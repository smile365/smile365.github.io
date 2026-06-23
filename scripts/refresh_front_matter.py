from __future__ import annotations

import argparse
import ast
import re
from collections import Counter
from pathlib import Path


POSTS_DIR = Path("content/posts")
CORE_KEYS = [
    "title",
    "keywords",
    "tags",
    "description",
    "categories",
    "heading",
]
GENERIC_TAGS = {
    "教程",
    "入门",
    "基础",
    "最新",
    "使用",
    "安装",
    "方法",
    "注意事项",
    "操作",
    "指南",
    "说明",
    "什么",
    "区别",
    "几个",
    "几种",
    "如何",
    "为什么",
    "以及",
    "这个",
    "那个",
    "真的",
    "一键",
    "推荐",
    "下载",
    "配置",
    "问题",
    "解决",
    "经验",
    "总结",
    "记录",
}
GENERIC_ENGLISH = {
    "and",
    "the",
    "for",
    "with",
    "from",
    "into",
    "your",
    "that",
    "this",
    "how",
    "what",
    "why",
    "when",
    "where",
    "who",
    "use",
    "using",
    "install",
    "setup",
    "guide",
    "tutorial",
    "introduction",
    "basic",
    "basics",
    "notes",
    "example",
    "examples",
    "demo",
    "issue",
    "error",
    "fix",
    "simple",
    "best",
    "new",
    "latest",
    "https",
    "http",
    "www",
    "com",
    "cn",
    "org",
    "net",
    "io",
    "html",
    "index",
    "enter",
    "description",
    "here",
}
TECH_HINTS = {
    "docker",
    "linux",
    "ubuntu",
    "debian",
    "centos",
    "mac",
    "macos",
    "windows",
    "python",
    "java",
    "golang",
    "go",
    "javascript",
    "typescript",
    "node",
    "nodejs",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",
    "hive",
    "hbase",
    "kafka",
    "elasticsearch",
    "es",
    "docker-compose",
    "k8s",
    "kubernetes",
    "hugo",
    "nginx",
    "openwrt",
    "git",
    "ssh",
    "wifi",
    "vnc",
    "raspberry",
    "raspberrypi",
    "树莓派",
    "编程",
    "代码",
    "开发",
    "运维",
    "服务器",
    "数据库",
    "接口",
    "抓包",
}
READ_HINTS = {
    "读书",
    "书",
    "小说",
    "影评",
    "剧评",
    "作者",
    "作品",
    "阅读",
    "看完",
    "豆瓣",
}
LIFE_HINTS = {
    "基金",
    "股票",
    "债",
    "生活",
    "旅行",
    "成都",
    "昆明",
    "租房",
    "减肥",
    "健康",
    "理财",
    "工作",
    "成长",
    "视频",
    "微信",
}
OTHER_HINTS = {
    "tiktok",
    "douyin",
    "affiliate",
    "awin",
    "cj",
    "注册",
    "reddit",
    "discord",
    "facebook",
    "paypal",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh post front matter for Hugo related content.")
    parser.add_argument("paths", nargs="*", help="Optional specific markdown files to process.")
    parser.add_argument("--write", action="store_true", help="Write changes back to files.")
    return parser.parse_args()


def split_front_matter(text: str) -> tuple[list[str], str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[4:end].splitlines(), text[body_start:]


def infer_title_from_body(body: str, fallback: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            return normalize_whitespace(re.sub(r"^#+\s*", "", stripped)) or fallback
        return normalize_whitespace(stripped[:80]) or fallback
    return fallback


def parse_front_matter(lines: list[str]) -> dict[str, object]:
    data: dict[str, object] = {}
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if not match:
            index += 1
            continue
        key = match.group(1)
        raw_value = match.group(2).strip()
        key_lower = key.lower()

        if raw_value == "":
            block_values = []
            probe = index + 1
            while probe < len(lines):
                item = lines[probe]
                if re.match(r"^\s*-\s+", item):
                    block_values.append(item.split("-", 1)[1].strip().strip('"'))
                    probe += 1
                    continue
                break
            if block_values:
                data[key_lower] = block_values
                index = probe
                continue
            data[key_lower] = ""
            index += 1
            continue

        if raw_value.startswith("[") and raw_value.endswith("]"):
            try:
                parsed = ast.literal_eval(raw_value)
            except Exception:
                parsed = []
            data[key_lower] = [str(item).strip() for item in parsed if str(item).strip()]
        else:
            data[key_lower] = raw_value.strip().strip('"')
        index += 1
    return data


def quote_yaml(value: str) -> str:
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def dump_list(values: list[str]) -> str:
    return "[" + ", ".join(quote_yaml(value) for value in values) + "]"


def normalize_whitespace(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^[#>*\-\d\.\s]+", "", text, flags=re.M)
    return normalize_whitespace(text)


def collect_existing_tags() -> set[str]:
    known_tags: set[str] = set()
    for path in POSTS_DIR.glob("*.md"):
        parsed = split_front_matter(path.read_text(encoding="utf-8"))
        if not parsed:
            continue
        fm_lines, _ = parsed
        data = parse_front_matter(fm_lines)
        for tag in data.get("tags", []):
            if isinstance(tag, str) and tag.strip():
                known_tags.add(tag.strip())
    return known_tags


def meaningful_description(description: str, title: str) -> bool:
    value = normalize_whitespace(strip_markdown(description))
    if not value:
        return False
    if value.lower() == title.lower():
        return False
    if len(value) < 8:
        return False
    if "http" in value.lower() or "[" in description or "](" in description:
        return False
    return True


def first_meaningful_paragraph(body: str) -> str:
    text = body.replace("\r\n", "\n")
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)
    paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", text)]
    for paragraph in paragraphs:
        if not paragraph:
            continue
        lines = [line.strip() for line in paragraph.splitlines() if line.strip()]
        if not lines:
            continue
        if all(line.startswith("#") for line in lines):
            continue
        if lines[0].startswith("!["):
            continue
        candidate = strip_markdown(" ".join(lines))
        if len(candidate) < 16:
            continue
        return candidate
    return ""


def shorten_description(text: str, limit: int = 88) -> str:
    if len(text) <= limit:
        return text
    sentence_match = re.match(rf"^(.{{20,{limit}}}?(?:[。！？]|(?<!\d)[.!?](?!\d)))", text)
    if sentence_match:
        return sentence_match.group(1)
    clipped = text[:limit].rstrip(" ,;:，；：")
    return clipped + "..."


def split_chinese_candidates(title: str) -> list[str]:
    raw = re.sub(r"[《》()（）【】\[\]：:|/]+", "|", title)
    raw = re.sub(r"[，,。！？!？、；;·-]+", "|", raw)
    raw = raw.replace("与", "|").replace("和", "|")
    parts = [segment.strip() for segment in raw.split("|") if segment.strip()]
    candidates: list[str] = []
    for part in parts:
        part = re.sub(r"^\d{2,4}年?", "", part)
        part = re.sub(r"(最新|基础|入门|教程|方法|指南|手册|操作手册|使用教程|新手注意事项|是什么|有什么区别|简明|一键|如何|谁更好|注意事项|最新安装和使用)", "|", part)
        for piece in part.split("|"):
            piece = normalize_whitespace(piece)
            piece = re.sub(r"[A-Za-z0-9.+#\-]+", " ", piece)
            piece = normalize_whitespace(piece)
            piece = re.sub(r"^[的了呢吗吧]", "", piece)
            piece = re.sub(r"[的了呢吗吧啊哦呀]$", "", piece)
            if len(piece) < 2 or len(piece) > 10:
                continue
            if piece in GENERIC_TAGS:
                continue
            candidates.append(piece)
    return candidates


def extract_english_phrases(text: str) -> list[str]:
    cleaned = strip_markdown(text)
    phrases = []
    cleaned = cleaned.replace("-", " ")
    for match in re.finditer(r"[A-Za-z][A-Za-z0-9.+#-]*(?:\s+[A-Za-z0-9.+#-]+){0,2}", cleaned):
        phrase = normalize_whitespace(match.group(0))
        lower = phrase.lower()
        compact = lower.replace(" ", "")
        if len(phrase) < 2:
            continue
        if lower in GENERIC_ENGLISH or compact in GENERIC_ENGLISH:
            continue
        if "." in phrase and phrase.count(".") >= 1:
            continue
        if phrase.lower() in {"ip", "ui", "os", "sd"}:
            continue
        if phrase.lower() == "enter description here":
            continue
        if re.search(r"\s\d+$", phrase):
            continue
        phrases.append(phrase)
    return phrases


def normalize_tag(value: str) -> str:
    value = normalize_whitespace(value)
    value = value.strip("-_/|,;:，；：。.!?[]()（）【】")
    if not value:
        return ""
    if re.fullmatch(r"\d+(?:\.\d+)?", value):
        return ""
    if re.fullmatch(r"[A-Z0-9-]{5,}", value):
        return ""
    if len(value) == 1 and not value.isascii():
        return ""
    if any(token in value.lower() for token in ["等外设", "谁更好", "gitee", "blogimg", "smile365", "sxy91", "logo", "xxxx"]):
        return ""
    return value


def infer_category(data: dict[str, object], title: str, body: str) -> list[str]:
    current = data.get("categories")
    lowered = (title + "\n" + body[:1200]).lower()
    if re.search(r"(^|[^a-z])books?([^a-z]|$)", lowered) or "读《" in title or "书单" in title:
        return ["read"]
    if isinstance(current, list) and current:
        values = [str(item).strip() for item in current if str(item).strip()]
        if values and values != ["other"]:
            return values
    if isinstance(current, str) and current.strip() and current.strip() != "other":
        return [current.strip()]
    if any(hint in lowered or hint in title for hint in TECH_HINTS):
        return ["code"]
    if any(hint in lowered for hint in OTHER_HINTS):
        return ["other"]
    if any(hint in title or hint in body[:1000] for hint in READ_HINTS):
        return ["read"]
    if any(hint in title or hint in body[:1000] for hint in LIFE_HINTS):
        return ["life"]
    return ["life"]


def infer_tags(title: str, heading: str, body: str, existing_tags: list[str], known_tags: set[str], categories: list[str]) -> list[str]:
    candidates: list[str] = []
    candidates.extend(existing_tags)
    candidates.extend(split_chinese_candidates(title))
    if heading and heading != title:
        candidates.extend(split_chinese_candidates(heading))

    english_pool = []
    english_pool.extend(extract_english_phrases(title))
    english_pool.extend(extract_english_phrases(heading))
    english_pool.extend(extract_english_phrases(body[:1600]))
    english_counts = Counter(english_pool)
    for phrase, _ in english_counts.most_common(8):
        candidates.append(phrase)

    normalized: list[str] = []
    seen: set[str] = set()
    for value in candidates:
        tag = normalize_tag(str(value))
        lower = tag.lower()
        if not tag:
            continue
        if lower in seen:
            continue
        if tag in GENERIC_TAGS or lower in GENERIC_ENGLISH:
            continue
        if len(tag) > 24 and all(ord(char) < 128 for char in tag):
            continue
        seen.add(lower)
        normalized.append(tag)

    curated: list[str] = []
    for tag in normalized:
        if tag in known_tags or tag.lower() in {item.lower() for item in known_tags}:
            curated.append(tag)
    for tag in normalized:
        if tag not in curated:
            curated.append(tag)

    if categories:
        if categories[0] == "code" and "教程" not in curated:
            curated.insert(0, "教程")
        elif categories[0] == "read" and "阅读" not in curated:
            curated.insert(0, "阅读")
        elif categories[0] == "life" and "生活" not in curated:
            curated.insert(0, "生活")
        elif categories[0] == "other" and "经验" not in curated:
            curated.insert(0, "经验")

    return curated[:8]


def infer_keywords(title: str, tags: list[str], body: str, slug: str) -> list[str]:
    keywords: list[str] = []
    keywords.extend(tags)
    title_terms = split_chinese_candidates(title)
    keywords.extend(title_terms[:4])
    english_terms = extract_english_phrases(title + " " + body[:800])
    keywords.extend(english_terms[:4])
    slug_terms = [part for part in re.split(r"[-_]+", slug) if len(part) > 2 and not part.isdigit()]
    keywords.extend(slug_terms[:3])

    result: list[str] = []
    seen: set[str] = set()
    for keyword in keywords:
        normalized = normalize_tag(str(keyword))
        lower = normalized.lower()
        if not normalized or lower in seen:
            continue
        seen.add(lower)
        result.append(normalized)
    return result[:10]


def render_front_matter(data: dict[str, object]) -> str:
    lines = ["---"]
    for key in CORE_KEYS:
        value = data.get(key)
        if key in {"keywords", "tags", "categories"}:
            items = value if isinstance(value, list) else []
            lines.append(f"{key}: {dump_list(items)}")
        else:
            lines.append(f"{key}: {quote_yaml(str(value or ''))}")

    remaining_keys = [key for key in data.keys() if key not in CORE_KEYS]
    for key in sorted(remaining_keys):
        value = data[key]
        if isinstance(value, list):
            lines.append(f"{key}: {dump_list([str(item) for item in value])}")
        else:
            lines.append(f"{key}: {quote_yaml(str(value))}")
    lines.append("---")
    return "\n".join(lines)


def process_file(path: Path, known_tags: set[str], write: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    source = original.lstrip("\ufeff\r\n")
    parsed = split_front_matter(source)
    if parsed:
        fm_lines, body = parsed
        data = parse_front_matter(fm_lines)
    else:
        body = source
        data = {}
    title = normalize_whitespace(str(data.get("title", "") or infer_title_from_body(body, path.stem)))
    heading_raw = normalize_whitespace(str(data.get("heading", "")))
    heading = heading_raw or title
    description_raw = normalize_whitespace(str(data.get("description", "")))
    if not meaningful_description(description_raw, title):
        description_source = first_meaningful_paragraph(body) or title
        description = shorten_description(description_source)
    else:
        description = shorten_description(normalize_whitespace(strip_markdown(description_raw)))

    existing_tags = data.get("tags") if isinstance(data.get("tags"), list) else []
    categories = infer_category(data, title, body)
    tags = infer_tags(title, heading, body, [str(item) for item in existing_tags], known_tags, categories)
    keywords = infer_keywords(title, tags, body, path.stem)

    data["title"] = title
    data["heading"] = heading
    data["description"] = description
    data["categories"] = categories
    data["tags"] = tags
    data["keywords"] = keywords

    rendered = render_front_matter(data)
    updated = rendered + "\n" + body.lstrip("\n")
    if updated == original:
        return False
    if write:
        path.write_text(updated, encoding="utf-8")
    else:
        print(f"=== {path} ===")
        print(rendered)
        print()
    return True


def main() -> None:
    args = parse_args()
    known_tags = collect_existing_tags()
    targets = [Path(path) for path in args.paths] if args.paths else sorted(POSTS_DIR.glob("*.md"))
    changed = 0
    for path in targets:
        if process_file(path, known_tags, args.write):
            changed += 1
    print(f"processed={len(targets)} changed={changed} write={args.write}")


if __name__ == "__main__":
    main()
# Pelican settings for the tiny-blogger static site.
# Local preview:  pelican content -s pelicanconf.py -r -l
# Production build is done by publishconf.py (used in GitHub Actions).

AUTHOR = 'Noah Seongjin Hwang'
SITENAME = "Noah.md"
SITESUBTITLE = "Code is cheap. Show me the Philosophy."   # 상단 바 제목 옆 부제. 비우면 표시 안 됨
SITEURL = ''            # empty for local preview; publishconf.py sets the real URL

PATH = 'content'
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

THEME = 'theme/tiny-blogger'
THEME_STATIC_DIR = 'static'

# --- URL scheme: same as tiny-blogger (/<category>/<slug>/ and /<category>/) ---
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Pages we do not generate (tiny-blogger has no tags/authors/archives).
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# index.html plus the client-side search page and its JSON index.
DIRECT_TEMPLATES = ['index', 'search', 'search_json']
SEARCH_SAVE_AS = 'search/index.html'
SEARCH_URL = 'search/'
SEARCH_JSON_SAVE_AS = 'search.json'

# --- Listing behaviour (mirrors tiny-blogger's Settings page) ---
DEFAULT_PAGINATION = 5
POSTS_TRUNCATE = True          # show a short excerpt on list pages instead of the full body
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Keep Korean (and other non-ASCII) characters in slugs, like tiny-blogger's slugify() did.
SLUGIFY_USE_UNICODE = True
SLUGIFY_PRESERVE_CASE = False

DEFAULT_CATEGORY = 'General'
USE_FOLDER_AS_CATEGORY = False

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Feeds are only generated in production (see publishconf.py).
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True

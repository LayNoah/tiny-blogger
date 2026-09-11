# 블로그 모양 바꾸기 — 명령어 가이드

모든 명령은 저장소 루트에서 실행한다.

```bash
cd ~/test/tiny-blogger
```

---

## 0. 기본 흐름 (항상 이 순서)

```bash
# 1) 미리보기 서버 켜기 (한 번만. 파일을 고치면 자동 반영됨)
source .venv/bin/activate
pelican content -s pelicanconf.py -r -l
#    → 브라우저에서 http://127.0.0.1:8000  (이전 모양이 남아 있으면 Ctrl+Shift+R)

# 2) 아래 표에서 원하는 항목의 명령을 실행해 파일을 열고, 값을 고치고, :wq

# 3) 마음에 들면 배포
git add -A
git commit -m "Tweak theme"
git push
#    → 1~2분 뒤 https://laynoah.github.io/tiny-blogger/ 반영
```

미리보기 서버 끄기: `Ctrl+C`

---

## 1. 빠른 찾기표

`vi +/검색어 파일` 은 그 검색어가 있는 줄에서 바로 열린다. 열린 뒤 `n` 을 누르면 다음 검색 결과로 이동.

| 바꾸고 싶은 것 | 명령 | 고칠 줄 |
| --- | --- | --- |
| 블로그 이름 (Noah.md) | `vi +/SITENAME pelicanconf.py` | `SITENAME = "Noah.md"` |
| 부제 (Talk is cheap...) 문구 | `vi +/SITESUBTITLE pelicanconf.py` | `SITESUBTITLE = "..."` (비우면 숨김) |
| 부제 굵기·크기·자간 | `vi +/navbar-tagline theme/tiny-blogger/static/css/style.css` | `font-weight` `font-size` `letter-spacing` |
| 구분 기호 `\|` 좌우 간격 (Noah.md↔`\|`, `\|`↔Talk) | `vi +/navbar-sep theme/tiny-blogger/static/css/style.css` | `margin-left` `margin-right` |
| 작성자 이름 (푸터 ©) | `vi +/AUTHOR pelicanconf.py` | `AUTHOR = '...'` |
| 상단 바 배경색 | `vi +/color-accent theme/tiny-blogger/static/css/style.css` | `--color-accent: #E35336;` |
| 카테고리(General) 글자색 | `vi +/color-category theme/tiny-blogger/static/css/style.css` | `--color-category: #000000;` |
| 글 제목(Hello, World!) 글자색 | `vi +/color-title theme/tiny-blogger/static/css/style.css` | `--color-title: #000000;` |
| 날짜(2026-09-11) 글자색 | `vi +/color-date theme/tiny-blogger/static/css/style.css` | `--color-date: #000000;` |
| 전체 글꼴 | `vi +/font-main: theme/tiny-blogger/static/css/style.css` | `--font-main: "NanumSquare", ...` |
| 블로그 이름 크기·굵기·자간·여백 | `vi '+/3-2\.' theme/tiny-blogger/static/css/style.css` | `font-size` `font-weight` `letter-spacing` `margin-left` `margin-top` |
| 메뉴(About/Categories/Search) 크기·오른쪽 여백 | `vi '+/3-3\.' theme/tiny-blogger/static/css/style.css` | `font-size` `margin-top` `margin-right` |
| 글 상세 페이지 폭 (한 줄 글자수) | `vi +/max-width theme/tiny-blogger/static/css/style.css` | `max-width: 50rem;` |
| 첫 화면 카드(글+이미지) 폭 | `vi +/content-home theme/tiny-blogger/static/css/style.css` | `max-width: 70rem;` |
| 카테고리(General) 크기·굵기 | `vi '+/5-1\.' theme/tiny-blogger/static/css/style.css` | `font-size` `font-weight` |
| 글 제목(Hello, World!) 크기·굵기 | `vi '+/5-2\.' theme/tiny-blogger/static/css/style.css` | `font-size` `font-weight` |
| 본문 글 크기·굵기·줄간격 | `vi '+/5-3\.' theme/tiny-blogger/static/css/style.css` | `font-size` `font-weight` `line-height` |
| 날짜(2026-09-11) 크기·굵기 | `vi '+/5-4\.' theme/tiny-blogger/static/css/style.css` | `font-size` `font-weight` |
| 대표 이미지 폭·위치·잘림 | `vi +/post-with-thumb theme/tiny-blogger/static/css/style.css` | `flex: 0 0 30rem` `gap` `margin-right` `padding-left` `padding-right` `row-reverse` `object-fit` |
| 첫 화면 글 순서 (카테고리→제목→본문→날짜) | `vi theme/tiny-blogger/templates/_article_list.html` | 블록 통째로 옮기기 (아래 4번) |
| 메뉴 순서·항목 추가 | `vi +/nav-item theme/tiny-blogger/templates/nav.html` | `<li>...</li>` 블록 (아래 5번) |
| 푸터 문구 | `vi theme/tiny-blogger/templates/footer.html` | `<small>` 안 (아래 6번) |
| 한 페이지 글 개수 | `vi +/DEFAULT_PAGINATION pelicanconf.py` | `DEFAULT_PAGINATION = 5` |
| 요약 대신 본문 전체 | `vi +/POSTS_TRUNCATE pelicanconf.py` | `POSTS_TRUNCATE = False` |

---

## 2. 색

`style.css` 맨 위 `2. 공통 설정` 의 변수 4개만 고친다. 색은 `#RRGGBB` 6자리.

```bash
vi +/color-accent theme/tiny-blogger/static/css/style.css
```

```css
--color-accent:   #E35336;  /* 상단 바 배경 + 링크에 마우스 올렸을 때 */
--color-category: #000000;  /* General */
--color-title:    #000000;  /* Hello, World! */
--color-date:     #000000;  /* 2026-09-11 */
```

상단 바 글자색(흰색)은 `3-2` 의 `color: #ffffff` (블로그 이름), `3-3` 의 `color: rgba(255,255,255,0.85)` (메뉴).
상단 바 아래 선을 다시 넣으려면 `3-1` 의 `border: 0 !important;` 줄을 지운다.

---

## 3. 글꼴

### 전체 글꼴 바꾸기

```bash
vi +/font-main: theme/tiny-blogger/static/css/style.css
```

```css
--font-main: "NanumSquare", "Pretendard", sans-serif;   /* 첫 번째 이름만 바꾼다 */
```

바로 쓸 수 있는 이름과 지원 굵기 (`2. 공통 설정` 주석에도 있음):

| 이름 | 느낌 | 굵기 |
| --- | --- | --- |
| `"NanumSquare"` | 나눔스퀘어. 저장소에 포함 | 300 400 700 800 |
| `"Pretendard"` | 곧고 깔끔한 고딕 | 100~900 |
| `"Noto Sans KR"` | 무난한 고딕 | 300 400 700 |
| `"IBM Plex Sans KR"` | 고딕, 영문 폭 넓음 | 300 400 700 |
| `"Nanum Gothic"` | 고딕 | 400 700 |
| `"Gowun Dodum"` | 둥근 고딕 | 400 |
| `"Nanum Myeongjo"` | 명조 | 400 700 |
| `"Gowun Batang"` | 바탕 | 400 700 |

### 특정 부분만 다른 글꼴

해당 섹션(예: 글 제목은 `5-2`)을 열고 `font-family: var(--font-main);` 을 `font-family: "Gowun Batang", serif;` 처럼 직접 적는다.

```bash
vi '+/5-2\.' theme/tiny-blogger/static/css/style.css
```

### 굵기

각 섹션의 `font-weight` 숫자. 300 가늘게, 400 보통, 700 굵게. 글꼴이 지원하지 않는 굵기는 가장 가까운 값으로 표시된다.

### 내 PC 글꼴 파일(ttf/otf) 추가

```bash
# 1) 파일 넣기 (예: MyFont-Light.ttf, MyFont-Regular.ttf)
cp ~/Downloads/MyFont-*.ttf theme/tiny-blogger/static/fonts/

# 2) 등록 줄 추가. 기존 줄을 복사해 파일명과 굵기만 바꾼다
vi +/@font-face theme/tiny-blogger/static/css/style.css
```

```css
@font-face { font-family: "MyFont"; font-weight: 300; font-display: swap; src: url("../fonts/MyFont-Light.ttf"); }
@font-face { font-family: "MyFont"; font-weight: 400; font-display: swap; src: url("../fonts/MyFont-Regular.ttf"); }
```

```bash
# 3) 글꼴 이름을 --font-main 첫 번째에
vi +/font-main: theme/tiny-blogger/static/css/style.css
```

(선택) 용량을 1/3로 줄이려면 ttf → woff2 변환 후 `url("../fonts/MyFont-Light.woff2") format("woff2")` 로:

```bash
pip install fonttools brotli
python3 - <<'PY'
from fontTools.ttLib import TTFont
import glob
for path in glob.glob("theme/tiny-blogger/static/fonts/*.ttf"):
    font = TTFont(path)
    font.flavor = "woff2"
    font.save(path[:-4] + ".woff2")
PY
```

### 정한 뒤 정리 (로딩 속도)

안 쓰는 외부 글꼴은 `base.html` 에서 지운다.

```bash
vi +/fonts.googleapis theme/tiny-blogger/templates/base.html
```

`&family=이름:wght@...` 항목 중 안 쓰는 것을 지우고, Pretendard 를 안 쓰면 `pretendard.min.css` 줄도 지운다.

---

## 4. 첫 화면 글 배치

```bash
vi theme/tiny-blogger/templates/_article_list.html
```

글 한 편은 아래 4개 블록으로 되어 있다. 순서를 바꾸려면 블록을 통째로 잘라(`V` 로 줄 선택 → `d`) 원하는 자리에 붙인다(`p`).

```html
<div class="post-meta post-category"> ... </div>   <!-- General -->
<h2> ... </h2>                                      <!-- Hello, World! -->
<p class="body"> ... </p>                           <!-- 본문 요약 -->
<div class="post-meta post-date"> ... </div>        <!-- 2026-09-11 -->
```

### 대표 이미지 (글 절반 + 이미지 절반)

글 md 파일 메타데이터에 `Image:` 한 줄 추가. 없는 글은 전체 폭으로 표시된다.

```bash
vi +/Slug content/posts/2026-09-11-hello-world.md
```

```markdown
Slug: hello-world
Image: https://lh3.googleusercontent.com/d/파일ID=w800-rw
```

이미지 칸 조절:

```bash
vi +/post-with-thumb theme/tiny-blogger/static/css/style.css
```

| 원하는 것 | 고칠 줄 |
| --- | --- |
| 글 칸 폭 (이미지는 나머지 전부) | `.post-text` 의 `flex: 0 0 30rem;` 숫자. 키우면 글이 왼쪽으로 넓어짐 |
| 글 전체를 왼쪽으로 옮기기 | `.post-text` 의 `margin-right: 0rem;` 숫자. 예) 3rem |
| 글 왼쪽 여백 (왼쪽 끝을 오른쪽으로) | `.post-text` 의 `padding-left: 0rem;` 숫자 |
| 글 오른쪽 여백 (오른쪽 끝을 왼쪽으로) | `.post-text` 의 `padding-right: 7rem;` 숫자 |
| 이미지 ↔ 글 간격 (글은 제자리, 이미지가 왼쪽으로 이동) | `gap: 1.5rem;` 숫자 |
| 이미지를 오른쪽으로 | `flex-direction: row-reverse;` → `row` |
| 빈 공간 없이 칸 꽉 채우기 (대신 잘림) | `object-fit: contain;` → `cover` |

### 그 외

| 원하는 것 | 명령 | 고칠 것 |
| --- | --- | --- |
| 요약 글자 수 | `vi +/truncate theme/tiny-blogger/templates/_article_list.html` | `truncate()` → `truncate(120)` |
| 글 사이 구분선 제거 | `vi +/hr theme/tiny-blogger/templates/_article_list.html` | `<hr>` 줄 삭제 |
| 오래된 글부터 | `vi pelicanconf.py` | 맨 아래에 `ARTICLE_ORDER_BY = 'date'` 추가 |

---

## 5. 상단 메뉴 (About / Categories / Search)

```bash
vi +/nav-item theme/tiny-blogger/templates/nav.html
```

`<li class="nav-item"> ... </li>` 블록 하나가 메뉴 하나다. 순서는 About(`pages` 반복문) → Categories → Search.

| 원하는 것 | 방법 |
| --- | --- |
| 순서 바꾸기 | `<li>...</li>` 블록을 잘라 붙이기 |
| 항목 추가 (예: GitHub) | `<li>` 하나 복사 후 `href` 와 글자만 바꾸기 |
| 메뉴 사이 간격 | `style.css` `3-3` 에 `.navbar .nav-item { margin: 0 .75rem; }` 추가 |
| 메뉴 전체 오른쪽 여백 | `style.css` `3-3` 의 `margin-right: 1rem;` |
| 메뉴를 왼쪽(제목 옆)으로 | `nav.html` 4행 `<div class="navbar-nav-scroll ml-auto"` 에서 `ml-auto` 삭제 |
| 블로그 이름을 정가운데로 | `style.css` `3-2` 아래 주석 처리된 `.navbar { position: relative; }` 블록의 `/*` `*/` 삭제 |

---

## 6. 푸터

```bash
vi theme/tiny-blogger/templates/footer.html
```

```html
<small class="text-muted">
  ©&nbsp;<span class="text-dark">{{ AUTHOR }}</span>      <!-- 이 줄을 원하는 문구로 -->
</small>
```

예: `<small class="text-muted">© 2026 {{ AUTHOR }}. All rights reserved.</small>`
정렬: `<footer class="text-center ...">` 의 `text-center` → `text-left` / `text-right`.

---

## 7. 글에 이미지 넣기 (구글 드라이브 링크)

저장소에 이미지를 올리지 않고 링크만 건다.

1. 드라이브에서 파일 우클릭 → 공유 → **링크가 있는 모든 사용자**
2. 공유 링크 `https://drive.google.com/file/d/`**`파일ID`**`/view?...` 에서 파일ID 복사
3. 글에 아래 형식으로 (공유 링크 그대로는 동작하지 않음)

```markdown
![설명](https://lh3.googleusercontent.com/d/파일ID=w800-rw)
```

- `w800` = 가로 800px 로 축소, `-rw` = webp 변환. 이 둘로 용량이 1/3, 로딩이 절반 이하가 된다.
- 폭 기준: 첫 화면 대표 이미지 `w800`, 본문 안 이미지 `w1600`.
- 드라이브에서 파일을 지우거나 공유를 끄면 글에서도 깨진다.

---

## 8. 자주 쓰는 vi 조작

| 키 | 동작 |
| --- | --- |
| `i` | 입력 시작 |
| `Esc` | 입력 종료 |
| `/글자` → `Enter` | 검색. `n` 다음, `N` 이전 |
| `V` → 화살표 → `d` | 줄 범위 잘라내기 |
| `p` | 붙이기 |
| `u` | 되돌리기 |
| `:wq` | 저장하고 닫기 |
| `:q!` | 저장 안 하고 닫기 |

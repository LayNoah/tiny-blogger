# 템플릿 수정 가이드

테마 파일은 `theme/tiny-blogger/` 아래에 있다. 수정 후 `pelican content -s pelicanconf.py -r -l` 로 미리 보고(`-r`이 템플릿/CSS 변경도 자동 반영), 마음에 들면 commit + push.

| 바꾸고 싶은 것 | 파일 |
| --- | --- |
| 블로그 제목 텍스트, 작성자 | `pelicanconf.py` (`SITENAME`, `AUTHOR`) |
| 제목 위치, 메뉴(About/Categories/Search) 위치·순서 | `theme/tiny-blogger/templates/nav.html` |
| 제목 라인(상단 바) 색, 글씨 크기, 글씨체 | `theme/tiny-blogger/static/css/style.css` |
| 푸터 문구 | `theme/tiny-blogger/templates/footer.html` |
| 글 목록 배치 | `theme/tiny-blogger/templates/_article_list.html` |
| 글 상세 페이지 배치 | `theme/tiny-blogger/templates/article.html` |
| 본문 폭, 외부 폰트 로드 | `theme/tiny-blogger/templates/base.html` |

Bootstrap은 **Bootswatch Lumen 4.6** 테마다(기본 색 `#158cba`, 기본 글꼴 Source Sans Pro). Bootstrap 클래스 이름은 https://getbootstrap.com/docs/4.6/ 에서 찾으면 된다. `style.css`는 `bootstrap.min.css` 뒤에 로드되므로 여기에 쓴 규칙이 Bootstrap을 덮어쓴다. 안 먹으면 `!important`를 붙인다.

---

## 1. 제목(블로그 이름) 위치

`nav.html` 2~3행:

```html
<nav class="navbar navbar-expand flex-column navbar-dark bg-primary">
  <a class="navbar-brand" href="{{ SITEURL }}/">{{ SITENAME }}</a>
```

- **제목 아래에 메뉴가 오는 현재 형태**: `flex-column` (기본값)
- **제목과 메뉴를 한 줄로 (제목 왼쪽, 메뉴 오른쪽)**: `flex-column` 삭제
  ```html
  <nav class="navbar navbar-expand navbar-dark bg-primary">
  ```
  메뉴를 오른쪽 끝으로 붙이려면 4행 `<div class="navbar-nav-scroll" id="navbarColor01">` 에 `ml-auto` 를 추가한다(`<ul>`에 붙이면 부모 div가 flex 자식이 아니어서 효과가 없다).
  ```html
  <div class="navbar-nav-scroll ml-auto" id="navbarColor01">
  ```
- **제목만 가운데 정렬**: `style.css`에 추가
  ```css
  .navbar-brand { margin: 0 auto; }
  ```
- **제목 글씨 크기**: `style.css`에 추가
  ```css
  .navbar-brand { font-size: 1.75rem; font-weight: 700; }
  ```

## 2. 글씨 크기 / 글씨체

`style.css` 맨 위 `body { ... }` 블록을 고친다.

```css
body {
    font-size: 1.0625rem;      /* 본문 크기. 1rem = 16px */
    line-height: 1.8;          /* 줄 간격 */
    font-family: "Noto Sans KR", "Source Sans Pro", sans-serif;
}
```

외부 폰트(예: Noto Sans KR, Pretendard)를 쓰려면 `base.html` `<head>` 안, `style.css` `<link>` **앞**에 한 줄 추가:

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
```

부분별 크기는 `style.css`에 선택자별로 추가:

```css
.post h2 { font-size: 1.5rem; }        /* 글 제목 (목록·상세 공통) */
.post .body { font-size: 1rem; }       /* 글 본문 */
.navbar .nav-link { font-size: 0.95rem; } /* 메뉴 글씨 */
```

## 3. 제목 라인(상단 바) 색

방법 A: Bootstrap 색 클래스 교체. `nav.html` 2행의 `bg-primary`를 바꾼다.
`bg-dark`, `bg-secondary`, `bg-success`, `bg-info`, `bg-warning`, `bg-danger`, `bg-light`, `bg-white`
밝은 배경(`bg-light`, `bg-white`)을 쓸 때는 글씨가 보이도록 `navbar-dark` → `navbar-light`.

방법 B: 원하는 색을 직접 지정. `style.css`에 추가.

```css
.navbar { background-color: #2c3e50 !important; }          /* 바 배경 */
.navbar-brand { color: #ffffff !important; }               /* 제목 색 */
.navbar .nav-link { color: rgba(255,255,255,.85) !important; } /* 메뉴 색 */
.navbar .nav-link:hover { color: #ffffff !important; }
```

글 제목(`text-primary`)이나 링크 색까지 한 번에 바꾸려면 Bootstrap 변수 대신 직접 덮어쓴다.

```css
a, .text-primary { color: #2c3e50 !important; }
```

## 4. About / Categories / Search 위치·순서

`nav.html`의 `<ul class="navbar-nav mr-auto">` 안에 `<li class="nav-item">` 블록 3개가 순서대로 About(7~10행, `pages` 반복문), Categories(11~18행), Search(19~21행)다.

- **순서 바꾸기**: `<li> ... </li>` 블록을 잘라 원하는 순서로 붙여 넣는다.
- **오른쪽 정렬**: `mr-auto` → `ml-auto`. **가운데 정렬**: `mr-auto` → `mx-auto`.
- **일부만 오른쪽으로 보내기**: `<ul>`을 두 개로 나눈다.
  ```html
  <ul class="navbar-nav mr-auto">   <!-- 왼쪽: About, Categories -->
    ...
  </ul>
  <ul class="navbar-nav ml-auto">   <!-- 오른쪽: Search -->
    ...
  </ul>
  ```
- **메뉴 사이 간격**: `style.css`에 `.navbar .nav-item { margin: 0 .75rem; }`
- **Categories를 드롭다운 대신 펼쳐서 나열**: 11~18행을 아래로 교체
  ```html
  {% for cat, cat_articles in categories %}
  <li class="nav-item">
    <a class="nav-link" href="{{ SITEURL }}/{{ cat.url }}">{{ cat.name }}</a>
  </li>
  {% endfor %}
  ```
- **메뉴 항목 추가** (예: GitHub 링크): `<li>` 하나 복사해서 `href`와 텍스트만 바꾼다.
- **About 등 고정 페이지 순서**: `content/pages/*.md` 파일에 `Order: 1` 같은 메타데이터를 넣고 `pelicanconf.py`에 `PAGE_ORDER_BY = 'order'` 추가.

## 5. 푸터 문구

`footer.html` 전체:

```html
<footer class="text-center pb-5">
  <small class="text-muted">
    ©&nbsp;<span class="text-dark">{{ AUTHOR }}</span>&nbsp;&nbsp;·&nbsp;&nbsp;Created with <a ...>tiny-blogger</a> &amp; <a ...>Pelican</a>
  </small>
</footer>
```

- 작성자 이름은 `pelicanconf.py`의 `AUTHOR`.
- 문구를 바꾸려면 `<small>` 안을 통째로 원하는 HTML로 교체. 예:
  ```html
  <small class="text-muted">© 2026 {{ AUTHOR }}. All rights reserved.</small>
  ```
- 위치: `text-center` → `text-left` / `text-right`. 여백: `pb-5` 숫자(0~5) 조절.

## 6. 글 배치

### 목록 페이지 (`_article_list.html`)

글 하나가 `<article class="post">` 블록이다. 기본 구조는 제목 → 날짜·카테고리 → 요약.

- **날짜를 제목 위로**: `<div class="text-muted">...</div>` 블록을 `<h2>` 앞으로 이동.
- **요약 길이**: `truncate()` → `truncate(120)` (글자 수). 요약 대신 전체 본문을 보이려면 `pelicanconf.py`의 `POSTS_TRUNCATE = False`.
- **글 사이 구분선 제거**: `{% if not loop.last %}<hr>{% endif %}` 삭제.
- **카드 형태로**: `<article class="post">` → `<article class="post card mb-4">` 로 바꾸고 `<header>`와 `<p class="body">`를 `<div class="card-body">` 로 감싼다.
- **2열 그리드**: 반복문 바깥을 `<div class="row">` 로 감싸고 `<article class="post col-md-6">`.
- **한 페이지에 보이는 글 수**: `pelicanconf.py`의 `DEFAULT_PAGINATION`.
- **정렬 순서**: 기본은 최신순. 오래된 글부터 보이려면 `pelicanconf.py`에 `ARTICLE_ORDER_BY = 'date'`.

### 상세 페이지 (`article.html`)

- 제목 색: `<h2 class="text-primary">` 의 `text-primary` 를 `text-dark` 등으로.
- 작성자 표시 제거: `<strong>{{ article.author or AUTHOR }}</strong> &nbsp;on&nbsp;` 삭제.
- 본문 위/아래 여백: `style.css`의 `.body { margin: 1rem 0; }`.

### 본문 폭 (`base.html`)

```html
<section class="content container" style="padding: 1rem 1.75rem; max-width: 50rem;">
```

`max-width` 숫자를 바꾼다. 넓게 `60rem`, 좁게 `42rem`.

---

## 확인하고 배포

```bash
source .venv/bin/activate
pelican content -s pelicanconf.py -r -l      # http://127.0.0.1:8000 에서 확인
git add theme pelicanconf.py
git commit -m "Tweak theme"
git push
```

브라우저에 이전 CSS가 남아 있으면 Ctrl+Shift+R 로 강제 새로고침.

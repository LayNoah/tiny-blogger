# Blog (static site)

tiny-blogger의 Bootstrap 템플릿(`blog/templates`)을 [Pelican](https://getpelican.com/) 테마로 옮긴 정적 블로그입니다.
GitHub Pages에 무료로 배포됩니다. Flask 앱(`../blog`)은 그대로 남아 있지만 배포에는 사용하지 않습니다.

```
site/
├── content/
│   ├── posts/      # 글 (Markdown)
│   ├── pages/      # About 같은 고정 페이지
│   └── images/     # 이미지 → /images/... 로 서빙
├── theme/tiny-blogger/
│   ├── templates/  # blog/templates 에서 포팅한 Jinja2 템플릿
│   └── static/     # bootstrap.min.css, style.css, 파비콘, search.js
├── pelicanconf.py  # 블로그 제목, 작성자, 페이지당 글 수 등
└── publishconf.py  # 배포용 설정 (SITEURL은 GitHub Actions가 넣어 줌)
```

## 글 쓰기

`content/posts/` 에 Markdown 파일을 추가합니다. 파일명은 자유입니다.

```markdown
Title: 글 제목
Date: 2026-09-11 13:00
Category: 일상
Slug: my-first-post

본문은 여기에 Markdown으로 씁니다. 이미지는 ![설명]({static}/images/photo.png)
```

- `Slug`를 생략하면 제목에서 자동 생성됩니다(한글 유지). URL은 `/<카테고리>/<slug>/` 입니다.
- `Category`는 자유롭게 적으면 자동으로 생성되고 상단 Categories 메뉴에 나타납니다.
- `Status: draft`를 넣으면 목록에 노출되지 않습니다.

## 로컬에서 미리 보기

```bash
cd site
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pelican content -s pelicanconf.py -r -l     # http://127.0.0.1:8000
```

## 배포

`master`에 push하면 `.github/workflows/pages.yml`이 빌드해서 GitHub Pages로 올립니다.

처음 한 번만 GitHub 저장소에서 설정합니다.

1. **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 변경
2. 주소를 `https://<계정>.github.io/` 로 쓰려면 저장소 이름을 `<계정>.github.io` 로 변경
   (그대로 두면 `https://<계정>.github.io/tiny-blogger/` 로 배포됩니다. 둘 다 자동 대응)
3. 커스텀 도메인은 **Settings → Pages → Custom domain**에 입력하고, DNS에 CNAME 레코드(`<계정>.github.io`)를 추가

## 설정 바꾸기

`pelicanconf.py`에서 수정합니다.

| 항목 | 설정 |
| --- | --- |
| 블로그 제목 | `SITENAME` |
| 푸터 작성자 | `AUTHOR` |
| 페이지당 글 수 | `DEFAULT_PAGINATION` |
| 목록에서 본문 요약 여부 | `POSTS_TRUNCATE` |

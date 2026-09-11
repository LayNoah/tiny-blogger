# Noah's Blog

Pelican 정적 블로그. `master`에 push하면 GitHub Actions가 빌드해서 https://laynoah.github.io/tiny-blogger/ 에 배포한다.

## 처음 한 번 (로컬 미리보기용)

```bash
cd site
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 글 쓰기

```bash
cd site
source .venv/bin/activate
vi content/posts/2026-09-11-my-post.md
```

파일 내용:

```markdown
Title: 글 제목
Date: 2026-09-11 13:00
Category: 일상
Slug: my-post

본문 (Markdown)
```

- URL은 `/<Category>/<Slug>/` 가 된다. `Slug`를 빼면 제목으로 자동 생성.
- 이미지는 `content/images/`에 넣고 `![설명]({static}/images/파일명.png)` 로 삽입.
- 아직 공개하지 않을 글은 `Status: draft` 한 줄 추가.

## 글 수정

```bash
vi site/content/posts/<파일명>.md
```

## 로컬에서 확인

```bash
cd site
source .venv/bin/activate
pelican content -s pelicanconf.py -r -l
# http://127.0.0.1:8000  (Ctrl+C 로 종료)
```

## 배포 (commit + push)

```bash
git add site/content
git commit -m "Post: 글 제목"
git push
```

push 후 1~2분 뒤 https://laynoah.github.io/tiny-blogger/ 에 반영된다.
진행 상황: https://github.com/LayNoah/tiny-blogger/actions

## 설정

`site/pelicanconf.py`

| 항목 | 값 |
| --- | --- |
| 블로그 제목 | `SITENAME` |
| 작성자 | `AUTHOR` |
| 페이지당 글 수 | `DEFAULT_PAGINATION` |
| 목록에 요약만 표시 | `POSTS_TRUNCATE` |

## 파일 위치

```
site/content/posts/     글
site/content/pages/     About 등 고정 페이지
site/content/images/    이미지
site/theme/tiny-blogger/  테마 (템플릿, CSS)
```

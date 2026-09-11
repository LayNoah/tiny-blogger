# Noah.md

Pelican 정적 블로그. `master` 에 push 하면 https://laynoah.github.io/tiny-blogger/ 에 자동 배포된다.
모양(색·글꼴·배치) 바꾸는 법은 [FixTemplate.md](FixTemplate.md).

## 처음 한 번

```bash
cd ~/test/tiny-blogger
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 새 글 쓰기

```bash
vi content/posts/2026-09-12-my-post.md
```

```markdown
Title: 글 제목
Date: 2026-09-12 13:00
Category: General
Slug: my-post
Image: https://lh3.googleusercontent.com/d/파일ID=w800-rw

본문. **굵게**, *기울임*, [링크](https://example.com)

## 소제목

- 목록
- 목록
```

- `Image:` 는 첫 화면에 나오는 대표 이미지. 없으면 글만 표시된다.
- 아직 안 올릴 글은 `Status: draft` 한 줄 추가.
- 글 주소는 `/General/my-post/` 가 된다.

## 이미지 넣기 (구글 드라이브)

1. 드라이브에서 파일 우클릭 → 공유 → **링크가 있는 모든 사용자**
2. 공유 링크 `https://drive.google.com/file/d/`**`파일ID`**`/view` 에서 파일ID 복사
3. 본문에:

```markdown
![설명](https://lh3.googleusercontent.com/d/파일ID=w1600-rw)
```

첫 화면 대표 이미지(`Image:`)는 `w800-rw`, 본문 안 이미지는 `w1600-rw`.

## 코드 넣기

문장 속 `코드` 는 백틱 하나로 감싼다.

여러 줄은 백틱 세 개로 감싸고 첫 줄에 언어 이름:

````markdown
```python
def hello():
    print("hi")
```
````

## 미리보기

```bash
source .venv/bin/activate
pelican content -s pelicanconf.py -r -l
# http://127.0.0.1:8000   (저장하면 자동 반영, Ctrl+C 로 종료)
```

## 배포

```bash
git add -A
git commit -m "Post: 글 제목"
git push
# 1~2분 뒤 https://laynoah.github.io/tiny-blogger/ 반영
# 진행 상황: https://github.com/LayNoah/tiny-blogger/actions
```

## 그 외

| 하고 싶은 것 | 명령 |
| --- | --- |
| 글 수정 | `vi content/posts/파일명.md` |
| 글 삭제 | `git rm content/posts/파일명.md` |
| About 페이지 수정 | `vi content/pages/about.md` |
| 블로그 이름·작성자 | `vi +/SITENAME pelicanconf.py` |

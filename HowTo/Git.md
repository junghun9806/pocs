# How to Start
## Setup 'config'
```bash
git config --global user.name "henrik"
git config --global user.email "henrik@unist.ac.kr"
git config --global core.editor "vim"
```

## Start 'local' repository
```bash
cd /base/path/to/manage
git init
git add .
git status  # see what's gonna staged.
git commit -m "Initial commit"
```
`git status`에서 출력된 내용을 보고, 관리하고 싶지 않은 파일이 staged 되었는지 확인하라. 만약 unstage하고 싶은 파일이 존재하면
1. Manual unstage `git rm --cached <file>..."`
2. Add to `.gitignore`

## Connect to 'remote' repository
### via HTTP and PAT
```bash
git remote add origin https://github.com/WooJoongKim0107/wjkim_bin.git
git remote set-url origin https://WooJoongKim0107:${token}@github.com/WooJoongKim0107/wjkim_bin.git
git push -u origin master
```

두번째의 `git remote set-url origin` 명령어는 personal access token을 필요로 한다는 것을 잊지 마라. GitHub 사이트의 우상단 프로필 사진을 클릭하여 settings로 접근, 좌측 사이드 바의 최하단 developer settings, 좌측 사이드바의 personal access token>Tokens(classic)으로 접근하여 token 생성, repo 권한 부여하여 생성된 token을 복사하여 위의 `${token}`에 대입하면 된다.

### via SSH and SSH Key
HTTP에 PAT를 사용하는 방식보단 이쪽이 더 안전하(다고하)고, 한번 GitHub 계정과 연결시켜놓으면 해당 device의 해당 계정에서는 계속 같은 `SSH key`를 사용할 수 있기 때문에 재사용성도 좋다. `git`을 자주 사용할 예정이라면 그냥 이렇게 한번 세팅해놓는 것을 추천한다.

1. GitHub 용 SSH key 생성 및 연결
과정은 [[SSH 연결 간략화 팁]]의 내용과 비슷하므로 자세한 설명은 생략한다.

GitHub repository와 연결하고 싶은 local device에서
```bash
ssh-keygen -t rsa -b 4096 -C "henrik@unist.ac.kr"
```

`~/.ssh/config`에 아래 문단 추가 (경로는 올바르게 수정)
```text
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_g
```

GitHub에 public key 등록
(1) GitHub 우상단 프로필사진 클릭; (2) settings; (3) 좌측 사이드바의 `SSH and GPG Keys` 클릭; (4) `New SSH Key`에 방금 생성된 `~/.ssh/id_rsa_g.pub`의 내용 붙여넣기

연결 테스트
```bash
ssh -T git@github.com
# Hi WooJoongKim0107! blabla
```

2. Remote repository와 연결
```bash
git remote add origin git@github.com:WooJoongKim0107/wjkim_bin.git
git push -u origin master
```

앞으로 새로운 폴더에서 `git`을 사용하게 되더라도, 같은 GitHub 계정의 repository를 remote로 연결할 때에는 위의 `git remote add origin ssh_url`만으로 연결이 가능하다. 만약 이미 HTTP + PAT로 연결된 상태라면
```bash
git remote set-url origin git@github.com:WooJoongKim0107/wjkim_bin.git
```
명령으로 주소를 변경할 수 있다.

---
## `git clone` instead of `git init`

Remote repository에 이미 최신 버전이 올라간 상태이고, 현재의 폴더는 그냥 그걸 다운받아서 시작하고 싶다면 그냥 `git clone`을 사용하면 된다.

```bash
git clone git@github.com:WooJoongKim0107/wjkim_Basics.git ~/Basics_sync
```

만약 `$HOME/Basics_sync`에 `.git`을 포함한 파일들을 배치하고 싶다면 위와 같이 실행하면 자동으로 `$HOME/Basics_sync` directory를 생성하고 그 안에 `.git` 및 파일들을 놓아두게 된다.

---
# Branch

새로운 기능을 만들 때에는 그냥 master branch에서 그대로 작업하기 보다는 새로운 branch에서 작업하는 것이 유용하다. 기능을 추가해보다가 만든 버그가 고쳐지지 않거나, 버그를 고치기 위해 정상 작동하는 backup을 사용할 필요가 생기기도 하기 때문이다.

## Branch 생성
```bash
git branch feature_json
# git checkout -b feature_json  # branch를 만들고 이동
```

## Branch 확인
```bash
git branch
```

## Branch 이동
```bash
git checkout branch  # 현재 branch에서 checkout하고 branch로 이동
# git checkout -b feature_json  # branch를 만들고 이동
```

Branch 신규 생성 시, 현재 branch와 같은 상태이므로 둘 간의 차이점은 아직 없다. 그러나 현재 보이는 working directory의 내용물은 현재의 branch에 귀속되므로, `feature_json` branch에서 코드를 수정하더라도, `git checkout master`로 돌아가면 정상 작동하던 과거의 상태로 돌아갈 수 있다.

## Branch 차이 확인
```bash
git log
git log --branches --decorate  # 버전 차이인지, 현재는 이게 default 같아 보인다.
git log -p master..feature_json  # 각 파일들의 `diff`도 확인
```

`git log -p master..feature_json`이 가장 자세한 정보를 알려줘서, 가장 자주 이용할 것 같다. 만약 branch가 조금 복잡해지거나 해서, 조금 간략하게 보고 싶으면 `--oneline` 옵션도 사용해보라.

## Merge
만약 신규 기능에 대한 확인이 끝나서, master branch에 변경 사항을 반영하고 싶다면, 먼저 master branch로 다시 이동해서 feature_json branch를 병합하면 된다.

```bash
git checkout master
git merge feature_json
git branch -d feature_json  # (optional) 사용 않는 branch 제거
```

---
## `git pull` & `git clone`

Remote repository와 working directory를 동기화 시키는 방법은 `git pull`과 `git clone`이 있다. 위에서 설명했듯이 `git clone`은 `git` 관리를 맨 처음 시작할 때 사용하는 것이므로, 대게의 경우 둘 중 어느 것을 할지 고민할 여지가 없다. 굳이 따지자면, 현재 디렉토리를 밀어버리고 다시 `git clone`을 하는 것과 그냥 `git pull`을 하는 방법이 있다.

1. `git pull`
`git pull`을 사용하면 `git`의 관리 하에 있는 파일들만 동기화 된다. 만약 `fileA.py`를 삭제한 commit이 존재하면, 현재 디렉토리에 있는 `fileA.py`는 삭제된다. 그러나 staging 되지 않은 파일들은 전혀 건들지 않으므로, 예를 들어 `.idea/`나 `.swp`처럼 `.gitignore`의 대상인 자료들은 현재 디렉토리에 그대로 잔존하게 된다.

2. `git clone`
`git clone` 자체의 특성은 아니지만, 밀어버리고 새로 가져오는 방식이기 때문에 `.idea/`나 `.swp` 같은 것들은 싹 삭제된 채로, 관리 대상인 자료들만 가져오게 된다.

---
## `git pull` vs `git fetch` + `git merge`

`git pull`은 `git fetch`와 `git merge`를 순차적으로 실행하는 것에 해당한다. `git fetch origin`은 remote repository에서 내용물을 다운 받는 것이고, 그 후 `git merge origin/master`를 통해 현재의 local repository를 remote repository의 내용물로 덮어쓴다. 만약 `git push` 과정을 깜빡하는 등의 이유로 local repository가 remote repository보다 앞선 상태이거나, 다른 이유로 remote repository의 내용을 당장 적용시키기 싫을 수 있다. 그런 경우에는 `git fetch origin` 이후 여러 차이점들을 살펴본 뒤 `git merge origin/master`를 수행한다.

```bash
git fetch origin/master
git log master..origin/master
git diff master..origin/master
# git merge origin/master
```

---
## `git log`로 현재 상태 확인하기

굳이 `git fetch` 이후 비교하는 방식이 아니더라도, 이미 up-to-date 상태인지 확인하는 것은 쉽다. GitHub commits 목록에서 가장 최근의 commit의 ID e.g. `1b28135`를 확인하고, 각각의 device에서 `git log` 명령어를 수행하여 가장 최신의 commit과 일치하는지 비교하면 된다.

```bash
git log
```

---
## `git reset` vs `git revert`

`git reset $(돌아갈 commit ID)`는 해당 시점으로 아예 돌아가버리는 것이고, `git revert $(취소할 commit ID)`는 해당 시점에 적용된 변경 사항들을 "역으로" 적용하여 변경 사항을 취소하는 것이다. 협업하는 내용에 대해서 `git reset`을 해버리면 아주 곤란해지므로, 그런 경우 보통 `git revert`만을 사용하지만, `git revert`는 특정 변경 사항을 취소했다는 새로운 commit이 생긴다. 따라서 그냥 혼자서 일하고 있고, 그냥 특정 commit 사이에 있던 일들을 아예 없던 것처럼 취소해버리고 싶을 때는 `git reset`을 쓴다. 물론 그 특성 상 매우 조심해야한다.

```bash
git reset --soft $(돌아갈 commit ID)
git reset --hard $(돌아갈 commit ID)
git reset --mixed $(돌아갈 commit ID)  # default
```

+ `--soft`: working directory의 파일들은 현 상태 그대로 남는 대신, staging 까지만 해둔 상태로 돌아감.
+ `--hard`: working directory의 파일들도 과거로 돌아감
+ `--mixed`: working directory의 파일들을 현 상태로 남겨두고, staging도 되지 않은 상태로 둠.

---
## 특정 파일 or 디렉토리 추적 중지

```bash
git rm --cached <file_path1> <file_path2> ...  # 파일 별
git rm --cached -r <directory_path>  # 폴더 내 recursive
```

---
## 현재의 변경 내용을 다른 branch에 적용

어떤 버그에 대한 fix가 간단할 것 같아서 master branch에서 작업하고 있었는데, 생각보다 필요한 변경 내용이 많다는 것을 뒤늦게 알아챘다고 하자. 그럼 현재의 변경 사항들을 master branch가 아니라 fix_bug branch에 commit하고, 기존의 master branch와의 sanity test를 진행할 필요가 있다.

이런 경우, 그냥 파일을 변경한 뒤에 새로운 branch를 만들고 거기에 commit 하면 된다. 작업하던 파일을 `:wq`로 저장하고 나온 뒤 `git status`를 하면 변경했으나 staging되지 않은 파일이 있다고 할 것이다. 바로 그 상태에서 새로운 branch `fix_bug`를 만들고 그곳으로 checkout한 뒤에 commit하면 된다.

```bash
git status
# ~~ 파일이 변경되었으나, staging 되지 않았다

git checkout -b fix_bug
git add .
git commit -m "TempFix bug"

git diff master fix_bug -- path/to/file
```

---
## 특정 파일의 branch 간 차이 확인

```bash
git diff branchA branchB -- path/to/file
```

---

## These tips are written by WooJoong Kim.

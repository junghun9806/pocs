# SSH config 사용하여 username, IP, port 입력 건너뛰기
### On Client (Windows)
1. `C:\Users\$username\.ssh\config` 파일에 (없으면 생성 후) 아래 내용 추가

```text
Host bellman
  HostName 10.xx.xx.xxx
  Port xxxxx
  User wjkim
```

이제 `ssh ssh://wjkim@10.xx.xx.xxx:xxxxx` 뿐만아니라 `ssh bellman`으로 접근하여 password를 입력하면 접속 가능하다. 

만약 tunneling이 필요하다면 `ProxyJump bellman` 형태의 line을 추가하면 된다.

# SSH key 사용하여 password 입력 건너뛰기
아래의 조치들을 수행하면 `ssh bellman`만 입력해도 접근 가능하다.
### On Client (Windows)
1. SSH key pair 생성하기
```text
ssh-keygen -t ed25519
```
중간에 passphrase 사용할지 물을텐데, 일종의 2차 비밀번호 개념이다. 보안을 위해 좋다하지만 그걸 설정하면 결국 passphrase를 입력해야 하게 되므로, 생략한다. `ssh-agent`라는 명령어를 통해 passphrase를 저장시켜서 이것마저 넘어가게 할 수 있으나, 애초에 교내 네트워크에서만 접근이 가능한 상태인데 너무 과한 조치라 생각하므로, passphrase는 생략한다.

2. SSH key 파일 위치 입력하기
```text
Host bellman
  HostName 10.xx.xx.xxx
  Port xxxxx
  User wjkim
  IdentityFile ~/.ssh/id_ed25519_1
```
여러 host를 저장할 때엔 그냥 empty line 한 줄 뒤에 같은 내용을 덧붙이면 되고, `id_ed25519_1`과 같은 ssh key는 여러 device에 공통으로 사용해도 상관은 없으나, 보안을 위해 별도로 만들어도 된다.

### On Host (Linux)
1. `.ssh/authorized_keys`에 SSH public key 추가하기

public key는 한 줄의 텍스트이며
authorized_keys의 line에 일치하는 key가 있는지 확인한다.
따라서 그냥 line을 복사하여 새 line에 붙여넣으면 된다.


# 일부 IP에 대해 password 입력 강제하기
1. Host (Linux)의 `/etc/ssh/sshd_config` 파일에 아래 내용 추가
```text
# 이건 어디에 commented out 되어 있을 것. 찾아서 comment 해제
PubkeyAuthentication yes

# 아래는 맨 마지막 줄에
# Public key related
## through VPN: require both if he uses public key
Match User wjkim Address 10.0.100.0/24
    AuthenticationMethods publickey,password

## through foreign IPs: public key cannot be used
Match User wjkim Address *,!10.0.100.0/24,!10.xx.yy.0/24,!10.xx.zz.0/24
    AuthenticationMethods password
```

2. `sudo systemctl restart sshd`

`ssh key`를 사용하는 유저 리스트를 `wjkim,jhchae` 형태로 붙여넣어라. 그리고 `10.xx.yy`와 `10.xx.zz`는 각각 서버실과 연구실의 IP를 세번째 옥텟까지로 대체해라. 그럼 public key를 사용하는 유저들에 대해 아래의 규칙이 적용된다.

> 1.  VPN으로 접속 시 반드시 public key와 password를 동시에 사용해야 한다.
> 2. 연구실이나 서버실에서 접속 시 public key와 password 중 하나만 써도 된다.
> 3. 이외의 IP에서 접속 시 반드시 password를 사용해야 한다. (public key를 무시)

### These tips are made by WooJoong Kim.
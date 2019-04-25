#
# build the infra in AWS

Make sure to change the group_vars/all
- replace the key with your public key

then run the following :

```
export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''
ansible-playbook provision.yml
```

#
# deploy/update the app
# 

* requires AWS to fetch the RDS db host dynamically

```
export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''
ansible-playbook -i "ip," deploy.yml`
```

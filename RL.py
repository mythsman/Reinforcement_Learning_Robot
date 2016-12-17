from copy import deepcopy
def value_certain_iteration():
	q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	table=[]
	table.append(deepcopy(q_val))
	while True:
		changed=False
		for i in range(1,5):
			left=0.5*max(q_val[i-1])
			if i==1:
				left+=1
			left=round(left,3)
			if left!=q_val[i][0]:
				changed=True
			q_val[i][0]=left
			right=0.5*max(q_val[i+1])
			if i==4:
				right+=5
			right=round(right,3)
			if right!=q_val[i][1]:
				changed=True
			q_val[i][1]=right
		table.append(deepcopy(q_val))
		if not changed:
			break
	policy=[0]
	for i in range(1,5):
		if q_val[i][0]>q_val[i][1]:
			policy.append(-1)
		else:
			policy.append(1)
	policy.append(0)
	return (table,policy)

#print(value_certain_iteration())

def value_random_iteration():
	q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	table=[]
	table.append(deepcopy(q_val))
	while True:
		changed=False
		for i in range(1,5):
			leftF=0.5*max(q_val[i-1])
			leftS=0.5*max(q_val[i])
			leftB=0.5*max(q_val[i+1])
			if i==1:
				leftF+=1
			if i==4:
				leftB+=5
			left=0.8*leftF+0.15*leftS+0.05*leftB
			left=round(left,3)
			if left!=q_val[i][0]:
				changed=True
			q_val[i][0]=left

			rightF=0.5*max(q_val[i+1])
			rightS=0.5*max(q_val[i])
			rightB=0.5*max(q_val[i-1])
			if i==1:
				rightB+=1
			if i==4:
				rightF+=5
			right=0.8*rightF+0.15*rightS+0.05*rightB
			right=round(right,3)
			if right!=q_val[i][1]:
				changed=True
			q_val[i][1]=right
		table.append(deepcopy(q_val))
		if not changed:
			break
	policy=[0]
	for i in range(1,5):
		if q_val[i][0]>q_val[i][1]:
			policy.append(-1)
		else:
			policy.append(1)
	policy.append(0)
	return (table,policy)

#print(value_random_iteration())

def policy_certain_iteration():
	policy=[0,1,1,1,1,0]
	q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	res=[]
	while True:
		table=[]
		q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
		while True:
			changed=False
			for i in range(1,5):
				left=0.5*q_val[i-1][policy[i-1]]
				right=0.5*q_val[i+1][policy[i+1]]
				if i==1:
					left+=1
				if i==4:
					right+=5
				left=round(left,3)
				right=round(right,3)
				if left!=q_val[i][0]:
					changed=True
				if right!=q_val[i][1]:
					changed=True
				q_val[i][0]=left
				q_val[i][1]=right
			table.append(deepcopy(q_val))
			if not changed:
				break
		new_policy=[0]
		for i in range(1,5):
			if q_val[i][0]<q_val[i][1]:
				new_policy.append(1)
			else:
				new_policy.append(-1)
		new_policy.append(0)
		res.append((table,new_policy))

		new_policy=[0]
		for i in range(1,5):
			if q_val[i][0]<q_val[i][1]:
				new_policy.append(1)
			else:
				new_policy.append(0)
		new_policy.append(0)
		if new_policy==policy:
			break
		else:
			policy=new_policy
	return res

# policy_certain_iteration()
def policy_random_iteration():
	policy=[0,1,1,1,1,0]
	q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	res=[]
	while True:
		q_val=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
		table=[]
		while True:
			changed=False
			for i in range(1,5):
				leftF=0.5*q_val[i-1][policy[i-1]]
				leftS=0.5*q_val[i][policy[i]]
				leftB=0.5*q_val[i+1][policy[i+1]]
				if i==1:
					leftF+=1
				if i==4:
					leftB+=5
				left=0.8*leftF+0.15*leftS+0.05*leftB
				left=round(left,3)
				if left!=q_val[i][0]:
					changed=True
				q_val[i][0]=left
	
				rightF=0.5*q_val[i+1][policy[i+1]]
				rightS=0.5*q_val[i][policy[i]]
				rightB=0.5*q_val[i-1][policy[i-1]]
				if i==1:
					rightB+=1
				if i==4:
					rightF+=5
				right=0.8*rightF+0.15*rightS+0.05*rightB
				right=round(right,3)
				if right!=q_val[i][1]:
					changed=True
				q_val[i][1]=right
			table.append(deepcopy(q_val))
			if not changed:
				break
		new_policy=[0]
		for i in range(1,5):
			if q_val[i][0]<q_val[i][1]:
				new_policy.append(1)
			else:
				new_policy.append(-1)
		new_policy.append(0)
		res.append((table,new_policy))
		new_policy=[0]
		for i in range(1,5):
			if q_val[i][0]<q_val[i][1]:
				new_policy.append(1)
			else:
				new_policy.append(0)
		new_policy.append(0)
		if new_policy==policy:
		    break
		else:
		    policy=new_policy
	return res

#policy_random_iteration()

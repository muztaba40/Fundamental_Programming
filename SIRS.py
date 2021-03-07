from numpy import zeros, linspace
import matplotlib.pyplot as plt

beta = 1./12     
alpha = 1./8
dt = 0.01             
D = 5            # Simulate for D days
N_t = int(D*24/dt)   # Corresponding no of hours
theta = 1./12

t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t+1)
I = zeros(N_t+1)
R = zeros(N_t+1)

# Initial condition
S[0] = 0.65
I[0] = 0.35
R[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n] + dt*theta*R[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*alpha*I[n]
    R[n+1] = R[n] + dt*alpha*I[n] - dt*theta*R[n]

fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper left')
plt.title('\u03B2 = 1/12,  \u03B1 = 1/8,  \u03B8 = 1/12')
plt.xlabel('time')
plt.ylabel('subpopulation')
plt.show()
plt.savefig('tmp.pdf'); plt.savefig('tmp.png')

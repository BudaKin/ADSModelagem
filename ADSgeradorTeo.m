a = [-0.4 0.2 0.1;
     0.3 -0.4 0.3;
     0.1 0.2 -0.4;
     1 1 1];

b = [0;0;0;1];

pi = a\b

Ocioso = pi(1)*100
Trafego_medio = pi(2)*100
Trafego_alto = pi(3)*100

T_medio = 0*pi(1) + 10*pi(2) + 50*pi(3) 
OPENQASM 2.0;
include "qelib1.inc";
gate rzx(param0) q0,q1 { h q1; cx q0,q1; rz(param0) q1; cx q0,q1; h q1; }
gate ecr q0,q1 { rzx(pi/4) q0,q1; x q0; rzx(-pi/4) q0,q1; }
qreg q[127];
creg c0[4];
creg meas[5];
rz(pi/2) q[41];
sx q[41];
rz(pi/2) q[41];
rz(pi/2) q[53];
sx q[53];
rz(pi/2) q[53];
rz(pi/2) q[59];
sx q[59];
rz(pi/2) q[59];
rz(pi/2) q[60];
sx q[60];
rz(pi/2) q[60];
x q[61];
barrier q[41],q[59],q[53],q[60],q[61];
sx q[41];
rz(-pi/2) q[41];
rz(-pi/2) q[53];
rz(-pi/2) q[59];
rz(-pi/4) q[60];
rz(-pi) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(3*pi/4) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
rz(-pi/2) q[60];
sx q[60];
rz(-3*pi/4) q[60];
sx q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[41];
rz(pi/2) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[41];
rz(-pi/2) q[53];
sx q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[53];
sx q[53];
rz(-pi/4) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
x q[53];
rz(-pi/2) q[53];
rz(-3*pi/4) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(3*pi/4) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[41];
rz(pi/2) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[41];
rz(-pi/2) q[53];
sx q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[53];
sx q[53];
rz(-3*pi/4) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(-3*pi/4) q[60];
sx q[60];
rz(pi/4) q[60];
sx q[60];
ecr q[53],q[60];
x q[53];
rz(-pi/2) q[53];
rz(pi/4) q[60];
sx q[60];
rz(-pi/4) q[60];
rz(-3*pi/4) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(-3*pi/4) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
rz(-pi/2) q[60];
sx q[60];
rz(-3*pi/4) q[60];
sx q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
rz(-3*pi/4) q[60];
sx q[60];
rz(pi/4) q[60];
sx q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(-pi/4) q[60];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
x q[53];
rz(pi/2) q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[53];
sx q[53];
rz(-pi/4) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(pi/4) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/4) q[53];
sx q[53];
rz(-pi) q[53];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
rz(-pi) q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(3*pi/8) q[53];
sx q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[41];
rz(pi/2) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[41];
rz(-pi/2) q[53];
sx q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[53];
sx q[53];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
rz(-7*pi/16) q[60];
rz(3*pi/4) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
rz(-9*pi/16) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
sx q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(-7*pi/16) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
rz(-9*pi/16) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
sx q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(-7*pi/16) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
sx q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-7*pi/8) q[53];
rz(-9*pi/16) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(-15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
sx q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
rz(-7*pi/8) q[59];
rz(-7*pi/16) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
x q[60];
rz(-pi/2) q[60];
rz(15*pi/16) q[61];
sx q[61];
rz(-pi) q[61];
ecr q[60],q[61];
rz(pi/2) q[60];
sx q[60];
rz(-5*pi/8) q[60];
sx q[60];
ecr q[53],q[60];
x q[53];
rz(-pi/2) q[53];
rz(7*pi/8) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
rz(pi/2) q[41];
rz(pi/2) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[41];
rz(-pi/2) q[53];
sx q[53];
ecr q[53],q[41];
rz(-pi) q[41];
sx q[41];
x q[53];
rz(pi/2) q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(pi/8) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[53];
sx q[53];
rz(-pi/8) q[53];
sx q[53];
sx q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(pi/8) q[53];
sx q[53];
ecr q[53],q[41];
sx q[41];
rz(pi/2) q[53];
sx q[53];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
sx q[59];
sx q[60];
rz(-pi/2) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[59],q[60];
rz(-pi/2) q[59];
rz(-pi) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[53],q[60];
x q[53];
rz(-pi/2) q[53];
rz(7*pi/8) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[59],q[60];
x q[59];
rz(-pi/2) q[59];
rz(-7*pi/8) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
rz(-pi) q[53];
rz(-pi/8) q[60];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
x q[53];
rz(pi/2) q[53];
ecr q[53],q[41];
sx q[41];
rz(-pi/2) q[53];
sx q[53];
rz(-pi/8) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi/8) q[53];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
rz(-pi) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[59],q[60];
rz(pi/2) q[59];
sx q[59];
rz(pi/2) q[59];
rz(-7*pi/8) q[60];
sx q[60];
rz(-pi) q[60];
ecr q[53],q[60];
x q[53];
rz(-pi/2) q[53];
rz(-pi/8) q[60];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
rz(pi/2) q[53];
sx q[53];
rz(-pi) q[60];
sx q[60];
rz(pi/2) q[60];
ecr q[53],q[60];
rz(-pi/2) q[53];
sx q[53];
sx q[60];
rz(-pi/2) q[60];
ecr q[53],q[60];
x q[53];
rz(pi/2) q[53];
ecr q[53],q[41];
rz(-pi) q[53];
rz(pi/2) q[60];
sx q[60];
rz(pi/2) q[60];
rz(pi/16) q[61];
barrier q[53],q[41],q[59],q[60],q[61];
measure q[53] -> meas[0];
measure q[41] -> meas[1];
measure q[59] -> meas[2];
measure q[60] -> meas[3];
measure q[61] -> meas[4];
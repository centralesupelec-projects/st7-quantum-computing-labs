OPENQASM 2.0;
include "qelib1.inc";
gate rzx(param0) q0,q1 { h q1; cx q0,q1; rz(param0) q1; cx q0,q1; h q1; }
gate ecr q0,q1 { rzx(pi/4) q0,q1; x q0; rzx(-pi/4) q0,q1; }
qreg q[127];
creg meas[2];
rz(pi/2) q[0];
sx q[0];
rz(-pi) q[1];
sx q[1];
rz(-pi) q[1];
ecr q[0],q[1];
x q[0];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
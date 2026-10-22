// SPDX-License-Identifier: MIT
const test=require('node:test'),a=require('node:assert/strict'),E=require('../src/engine');
test('modelo inicial e informe sin avisos',()=>{let m=E.sample();a.equal(E.validateModel(m),true);a.deepEqual(E.diagnostics(m),[]);});
test('receptividades booleanas sin evaluación dinámica',()=>{a.equal(E.evalCondition(E.parseCondition('a AND NOT b'),{a:true,b:false}),true);a.throws(()=>E.parseCondition('a; alert(1)'),/./);});
test('secuencias de la instalación de envasado',()=>{let m=E.sample(),s=E.initialState(m);m.inputs.marcha=true;s=E.advance(m,s);a.deepEqual(s.active,['E1']);m.inputs.carga_terminada=true;s=E.advance(m,s);a.deepEqual(s.active,['E2']);a.deepEqual(s.outputs,['RESISTENCIA_SELLO']);});
test('sin receptividad, sin avance',()=>{const m=E.sample();let x=E.advance(m,E.initialState(m));a.deepEqual(x.active,['E0']);a.equal(x.status,'waiting');});
test('divergencia ambigua se bloquea',()=>{let m=E.sample();m.inputs.marcha=true;m.transitions.push({id:'T9',name:'Alternativa',from:['E0'],to:['E3'],condition:'1'});let s=E.advance(m,E.initialState(m));a.equal(s.status,'conflict');a.deepEqual(s.active,['E0']);});
test('disparo simultáneo de transiciones independientes',()=>{let m=E.sample();m.stages[1].initial=true;m.transitions[0].condition='1';m.transitions[1].condition='1';m.inputs=E.collectInputs(m);let s=E.advance(m,E.initialState(m));a.equal(s.status,'fired');a.deepEqual(s.active,['E1','E2']);a.deepEqual(s.last,['T0','T1']);});

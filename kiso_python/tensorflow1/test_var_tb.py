# -*- coding: utf-8 -*-

import tensorflow as tf

# 変数を定義
v = tf.Variable(0, name='v')

# 定数を定義
a = tf.constant(10, name='10')
b = tf.constant(20, name='20')

# 演算を定義
mul_op = tf.multiply(a, b, name='mul')
assign_op = tf.assign(v, mul_op)

sess = tf.Session()
sess.run(assign_op)

tf.summary.FileWriter('./logs', sess.graph)

res = sess.run(v)
print(res)
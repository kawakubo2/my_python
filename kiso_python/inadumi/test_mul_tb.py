# -*- coding: utf-8 -*-

import tensorflow as tf

tf.reset_default_graph()

a = tf.constant(10, name='10')
b = tf.constant(20, name='20')
c = tf.constant(30, name='30')

sub_op = tf.subtract(a, b, name='sub')
mul_op = tf.multiply(sub_op, c, name='mul')

sess = tf.Session()
res = sess.run(mul_op)
print(res)


tf.summary.FileWriter('./logs', sess.graph)

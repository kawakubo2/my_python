import tensorflow as tf

a = tf.constant(10, name='10')
b = tf.constant(20, name='20')
c = tf.constant(30, name='30')

add_op = tf.add(a, b, name='add')
mul_op = tf.multiply(add_op, c, name='mul')

sess = tf.Session()
res = sess.run(mul_op)
print(res)

tf.summary.FileWriter('./logs', sess.graph)
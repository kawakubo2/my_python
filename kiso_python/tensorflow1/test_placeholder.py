# -*- coding: utf-8 -*-

import tensorflow as tf

# プレースホルダを定義
a = tf.placeholder(tf.int32, [5])

# ベクトルを2倍にする演算を定義
two = tf.constant(2)
x2_op = a * two

# セッションを開始
sess = tf.Session()

# プレースホルダに値を当てはめて実行
res1 = sess.run(x2_op, feed_dict={a: [1, 2, 3, 4, 5]})
print(res1)
res2 = sess.run(x2_op, feed_dict={a: [5, 6, 7, 10, 100]})
print(res2)
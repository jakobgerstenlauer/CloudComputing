import numpy as np

num_puntos = 100
conjunto_puntos = []
for i in range(num_puntos):
    x1 = np.random.normal(0.0, 0.9)
    y1 = x1 * 0.3 + 0.9 + np.random.normal(0.0, 0.05)
    conjunto_puntos.append([x1, y1])

x_data = [v[0] for v in conjunto_puntos]
y_data = [v[1] for v in conjunto_puntos]

import matplotlib.pyplot as plt

# Graphic display
plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.savefig("InputPointsRegression.jpg")

import tensorflow as tf

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(101):
    sess.run(train)
    if step % 1 == 0:
        print(step, sess.run(W), sess.run(b))
	plt.plot(x_data, y_data, 'ro')
	plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
	plt.legend()
	plt.savefig('Intermediate_Regression_Results_' + str(step) + '.jpeg')
	
plt.plot(x_data, y_data, 'ro')
plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
plt.legend()
plt.savefig('RegressionResults.jpeg')


import tensorflow as tf

session = tf.Session()

# Constant nodes
# When and how to use them
# Sessions
# Constant nodes store non-changeable values
# Sessions evaluate the tensor value of a node

# const_1 = tf.constant(value=[[1.0, 2.0]],
#                       dtype=tf.float32,
#                       shape=(1, 2),
#                       name='const_1',
#                       verify_shape=True)
# const_2 = tf.constant(value=[[3.0, 4.0]],
#                       dtype=tf.float32,
#                       shape=(1, 2),
#                       name='const_2',
#                       verify_shape=True)
#
#
# print(session.run(fetches=[const_1, const_2]))

# Variable nodes
# When and how to use them
# Compare to constant nodes
# Variables nodes store values that can change

# var_1 = tf.Variable(initial_value=[1.0],
#                     trainable=True,
#                     collections=None,
#                     validate_shape=True,
#                     caching_device=None,
#                     name='var_1',
#                     variable_def=None,
#                     dtype=tf.float32,
#                     expected_shape=(1, None),
#                     import_scope=None)
#
# print(var_1)
# init = tf.global_variables_initializer()
# session.run(init)
# print(session.run(fetches=var_1))
#
# var_2 = var_1.assign(value=[2.0])
# print(session.run(fetches=var_1))
# print(session.run(fetches=var_2))

# Placeholder nodes
# When and how to use them
# Compare to constant and variable nodes
# Placeholder nodes act as inputs to the computational graph

# placeholder_1 = tf.placeholder(dtype=tf.float32,
#                                shape=(1, 4),
#                                name='placeholder_1')
#
# placeholder_2 = tf.placeholder(dtype=tf.float32,
#                                shape=(2, 2),
#                                name='placeholder_2')
#
# print(placeholder_1)
# print(session.run(fetches=[placeholder_1, placeholder_2],
#                   feed_dict={placeholder_1: [[1.0, 2.0, 3.0, 4.0]], placeholder_2: [[1.0, 2.0], [3.0, 4.0]]}))

# Operation nodes
# How to perform operations on existing nodes
# Build a mini computational graph
# Operation nodes perform some operation on one or more nodes and store result

# const_1 = tf.constant(value=[1.0])
# const_2 = tf.constant(value=[2.0])
# placeholder_1 = tf.placeholder(dtype=tf.float32)
# # results = const_1 + const_2
# results = tf.add(x=placeholder_1, y=const_2, name='results')
#
# # y = Wx + b
# W = tf.constant(value=[2.0])
# b = tf.constant(value=[1.0])
# x = tf.placeholder(dtype=tf.float32)
# # y = W * x + b
# mult = tf.multiply(x=W, y=x)
# y = tf.add(x=mult, y=b)
#
# # print(session.run(fetches=results, feed_dict={placeholder_1: [2.0]}))
# print(session.run(fetches=y, feed_dict={x: [2.0, 3.0, 4.0]}))

# Loss functions and optimizers
# Training and testing
# Introduce the concepts and look at some examples

# # loss function: actual vs expected outputs
# # actual: output from our model given an input
# # expected: correct output given an input
#
# # Optimizers: change values in model to alter loss (typically to minimize)
#
# # Values altered during training
# # Model assessed during testing
#
# x_train = [1.0, 2.0, 3.0, 4.0]
# y_train = [2.0, 3.0, 4.0, 5.0]
# y_actual = [1.5, 2.5, 3.5, 4.5]
# loss = tf.reduce_sum(input_tensor=tf.square(x=y_train - y_actual))
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05)
# train_step = optimizer.minimize(loss=loss)

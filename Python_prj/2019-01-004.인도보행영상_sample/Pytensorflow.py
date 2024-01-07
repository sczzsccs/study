import tensorflow as tf
import numpy as np

# 훈련 데이터 생성
X_train = np.array([1, 2, 3, 4, 5], dtype=np.float32)
y_train = np.array([2, 4, 6, 8, 10], dtype=np.float32)

# 가중치와 편향 변수 정의
W = tf.Variable(0.0)
b = tf.Variable(0.0)

# 손실 함수 정의
def loss_fn(inputs, targets):
    predictions = W * inputs + b
    loss = tf.reduce_mean(tf.square(predictions - targets))
    return loss

# 옵티마이저 정의
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# 학습 과정
for epoch in range(100):
    with tf.GradientTape() as tape:
        loss = loss_fn(X_train, y_train)
    gradients = tape.gradient(loss, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))

# 학습 결과 출력
print("W =", W.numpy())
print("b =", b.numpy())

import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

# CIFAR-10 데이터셋 로드
dataset = tfds.load('cifar10', split='train', shuffle_files=True)

# 데이터 확인
fig = plt.figure(figsize=(10, 10))
for i, data in enumerate(dataset.take(25)):
    image, label = data['image'], data['label']
    ax = fig.add_subplot(5, 5, i+1)
    ax.imshow(image)
    ax.set_title(label.numpy())
    ax.axis('off')

plt.show()
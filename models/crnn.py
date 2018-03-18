from keras.layers import Input, Flatten, Conv2D, LSTM, Activation, MaxPooling2D, Dense, BatchNormalization
from keras.optimizers import Adam
from keras.models import Model

def crnn(input_shape, output_shape):
    inputs = Input(input_shape)
    
    x = Conv2D(8, (3,3), padding='same')(inputs)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D((3,3),padding='same')(x)

    x = Conv2D(8, (3,3), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D((3,3),padding='same')(x)
    
    x = Flatten()(x)

    #x = LSTM(32)(x)
    x = Dense(output_shape[0], activation='sigmoid')(x)

    model = Model(inputs=inputs, outputs=x)
    model.compile(optimizer=Adam(lr=1e-4),
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])
    return model

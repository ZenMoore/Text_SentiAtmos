## info for the best model


* running config:
```
--max_seq_length=128
--train_batch_size=32
--learning_rate=2e-5
--num_train_epochs=3.0
```

* albert config
```
albert_tiny_zh
--config=original
```

* follow-net config
```
Multi-RNN
--num_layers = 3  
--hidden_dim = 128  
--rnn = 'lstm'  
--dropout_keep_prob = 0.8
--hidden_dropout_keep_prob = 1.0 
--batch_size = 128  
--num_epochs = 10  
```
# OOPLearning
## class可以单独添加 key和value （laptop例子，加discount）
> m4800.bluetooth = 'yes'
> 
> print(m4800.__dict__)
> 
> {'name': 'm4800', 'price': 55000, 'bluetooth': 'yes'}

## __init__里的不会自动更新（保持初始值），想要自动更新需要单独建立method
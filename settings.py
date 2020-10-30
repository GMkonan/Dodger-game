class Settings():
    def __init__(self):
        #player model vars
        self.playerx = 370
        self.playery = 500 #por causa do tamanho da imagem
        self.playerx_change = 0
        self.playery_change = 0

        #enemy model vars
        self.enemyimg = []
        self.enemyx = []
        self.enemyy = []
        self.enemyy_change = []
        self.num_of_enemies = 10

        self.life = 3
        self.damage = 1
        self.score = 0

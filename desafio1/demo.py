from modulos.mario import Mario
from modulos.luigi import Luigi
from modulos.KoopaTroopa import Koopa
from modulos.Goomba import Goomba

mario=Mario()
mario.mover(3,4)
mario.lanzar_fuego()
mario.saltar()

luigi=luigi()
luigi.mover(5,6)
luigi.lanzar_honguitos()
luigi.saltar()

koopa=Koopa()
koopa.mover(1,2)
koopa.volar()
koopa.dano(print("genera un daño del 10%"))
koopa.atacar(print("bellotas"))

goomba=Goomba()
goomba.atacar(print("rayos"))
goomba.escudo()
goomba.mover(4,5)
goomba.dano(print("genera un daño del 50%"))

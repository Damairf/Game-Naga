import random
import time

class Character:
    def __init__(self, hp, potion):
        self.hp = hp
        self.potion = potion

    def attack(self):
        damage = random.randint(50, 400)
        if damage > 300:
            print("CRITICAL HIT!")
        return damage

    def drink_potion(self):
        if self.potion > 0:
            potion = random.randint(30, 50)
            self.potion -= 1
            self.hp += potion
            return True
        else:
            print("sayang sekali potionmu habis!")
            return False

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_potion(self):
        return self.potion

    def set_potion(self, potion):
        self.potion = potion

class PortalDragonGame:
    def __init__(self):
        self.naga_baik = random.randint(1, 2)
        self.naga_jahat = 2 if self.naga_baik == 1 else 1
        self.kesempatan_kabur = random.randint(1, 50)

        self.player = Character(200, 4)
        self.naga = Character(2000, 0)

    def play(self):
        print("Kamu melihat dua portal di depanmu ...")
        time.sleep(1)
        portal = int(input("Apakah kamu memilih portal 1 atau 2?"))

        if portal == self.naga_baik:
            print("Portal ini sangat gelap, kamu tidak bisa melihat apa-apa")
            time.sleep(1)
            print("Kamu mendengar ada suara langkah yang datang ke arahmu")
            time.sleep(1)
            print("Tiba-tiba ada sesosok naga HITAM yang berdiri dihadapanmu")
            time.sleep(1)
            print("Naga tersebut membuka mulutnya dan...")
            time.sleep(1)
            print("Isi mulutnya berisi harta yang ingin dibagikan kepadamu, selamat kamu menemukan naga yang ramah")

        elif portal == self.naga_jahat:
            print("Di dalam portal tersebut tedapat naga HITAM yang datang menghampirimu dengan tatapan penuh amarah")
            time.sleep(1)
            decision = input("Apakah kau akan 'kabur' atau 'melawan' naga itu?")

            if decision == "kabur":
                if self.kesempatan_kabur >= 24:
                    print("Kamu berhasil kabur dari sergapan naga jahat itu")
                else:
                    print("Naga itu berhasil menangkapmu dan kau dibunuh")
                    return
            elif decision == "melawan":
                print("Sepertinya pedang yang kamu bawa berguna juga")
                time.sleep(1)

                while self.naga.get_hp() > 0 and self.player.get_hp() > 0:
                    print("Ender Dragon:", self.naga.get_hp())
                    print("Kau memiliki HP:", self.player.get_hp(), "dan jumlah potion", self.player.get_potion())

                    battle = int(input("1.Serang 2.Minum potion"))
                    if battle == 1:
                        self.naga.set_hp(self.naga.get_hp() - self.player.attack())
                    elif battle == 2:
                        if not self.player.drink_potion():
                            continue

                    # Dragon Phase
                    if self.player.get_hp() > 0:
                        dragon_chance = random.randint(0, 100)
                        if dragon_chance > 18:
                            dragon_damage = random.randint(8, 45)
                            self.player.set_hp(self.player.get_hp() - dragon_damage)
                            print("Naga itu menyerangmu, menyisakanmu", self.player.get_hp(), "HP")
                        else:
                            print("BERUNTUNG SEKALI! Naga itu meleset")

                if self.player.get_hp() <= 0:
                    print("Sayang sekali kamu telah dikalahkan oleh sang Ender Dragon")
                    if self.naga.get_hp() < 300:
                        print("Padahal kamu hampir mengalahkannya")
                    time.sleep(1)
                    print("GAME OVER")

                if self.naga.get_hp() <= 0:
                    print("SELAMAT kamu mengalahkan sang Ender Dragon dan mendapat telur Ender Dragon")

game = PortalDragonGame()
game.play()
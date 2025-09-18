import discord
from discord.ext import commands
from model import get_class
import os
import random
import string
import operator


# Variable Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
theRole = "Go Green"

# Tabel foto
plastik = ["./Pictures/karyaplastik.jpeg", "./Pictures/karyaplastik1.jpeg"]
kertas = ["./Pictures/karyakertas.jpeg", "./Pictures/karyakertas1.jpeg"]
kaca = ["./Pictures/karyakaca.jpeg", "./Pictures/karyakaca1.jpeg"]
kardus = ["./Pictures/karyakardus.jpeg", "./Pictures/karyakardus1.jpeg"]
ban = ["./Pictures/karyaban.jpeg", "./Pictures/karyaban1.jpeg"]
botol = ["./Pictures/karyabotol.jpeg", "./Pictures/karyabotol1.jpeg"]
kaleng = ["./Pictures/karyakaleng.jpeg", "./Pictures/karyakaleng1.jpeg"]

        

class hitung_num:
    def tambah(self, x, y):
        return x + y
    def kurang(self, x, y):
        return  x - y
    def kali(self, x, y):
        return  x * y
    def bagi(self, x, y):
        result = round(x / y, 2) # membulatkan hasil bagi menjadi 2 desimal(dari 3.14159 menjadi 3.14)
        if isinstance(result, float) and result.is_integer(): # sebagai double check apakah float(2.0) adalah int/bilangan bulat(2)
            return int(result)
        return result
    def pangkat(self, x, y):
        return  x ** y
    
@bot.event
async def on_ready():
    print(f'{bot.user} sudah siap dioperasikan.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!!  Namaku {bot.user}!')

@bot.command()
async def hitung(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    await ctx.send("Mau tambah, kurang, kali, bagi, atau pangkat?")
    m = await bot.wait_for('message', check=check)
    wordCheck = ('tambah', 'kurang', 'kali', 'bagi', 'pangkat', '+', '-', 'x', ':', '^', 'add', 'subtract', 'multiply', 'divide', 'power')
    if m.content.lower() in wordCheck:
        await ctx.send("Berikan angka yang ingin dihitung.")
        msuno = await bot.wait_for('message', check=check)
        await ctx.send("Satu lagi.")
        msdos = await bot.wait_for('message', check=check)
        try:
            numero = int(msuno.content)
            numeros = int(msdos.content)
            result = hitung_num()
            if m.content.lower() in ["tambah", "+", "add"]:
                await ctx.send(f"{numero} + {numeros} hasilnya {result.tambah(numero, numeros)}.")

            if m.content.lower() in ["kurang", "-", "subtract"]:
                await ctx.send(f"{numero} - {numeros} hasilnya {result.kurang(numero, numeros)}.")
            
            if m.content.lower() in  ["kali", "x", "multiply"]:
                await ctx.send(f"{numero} x {numeros} hasilnya {result.kali(numero, numeros)}.")
            
            if m.content.lower() in ["bagi", ":", "divide"]:
                await ctx.send(f"{numero} : {numeros} hasilnya {result.bagi(numero, numeros)}.")
            
            if m.content.lower() in ["pangkat", "^", "power"]:
                await ctx.send(f"{numero} pangkat {numeros} hasilnya {result.pangkat(numero, numeros)}.")
        except:
            await ctx.send("Anda tidak memasukkan angka yang valid!")
            await ctx.send("Coba lagi!")
    else:
        await ctx.send("Anda tidak memasukkan perintah yang jelas/typo.")


@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=theRole)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} sekarang menjadi role {theRole}!")
    else:
        await ctx.send("Role nggak ada!")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=theRole)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} dihapuskan dari role {theRole}.")
    else:
        await ctx.send("Role nggak ada!")

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f'You said: "{msg}".')

@bot.command()
async def make_pass(ctx, length=6):
    alphabets = list(string.ascii_letters + string.digits)
    result = ''
    for i in range(length):
        addword = random.choice(alphabets)
        str(addword)
        result += addword
    await ctx.send(f"Ini passwordnya: {result}")


@bot.command()
async def tips(ctx):
    lifeTips = [
        'Pisahkan sampah organik dan anorganik untuk mempermudah tukang sampah memisahkannya.',
        'Terapkan 3R(reuse, reduce, recycle) dalam kehidupan sehari hari.',
        'Buat kompos dari sampah organik seperti daun kering atau sisa sayuran.',
        'Kurangi pemakaian barang sekali pakai seperti gelas plastik dan gunakan tumbler/tempat minum sendiri.',
        'Sering-sering mampir ke bank sampah untuk mendaur ulang sampah anorganik & organik anda.',
        'Anda bisa memisahkan sampah organik untuk dijadikan pupuk dengan menggunakan komposter',
        'Pastikan anda membuang sampah pada tempatnya dan bukan di jalan atau tempat selain untuk menaruh sampah.'
    ]
    await ctx.send(random.choice(lifeTips))

@bot.command()
async def question(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    pertanyaan_list = [
        "Sampah plastik termasuk sampah organik atau anorganik?",
        "Sampah rokok termasuk sampah B3 atau tidak?",
        "Sampah organik adalah sampah yang?",
        "Proses penguraian sampah organik disebut?",
        "Lambang 3R dalam pengelolaan sampah adalah?",
        "Salah satu dampak dari membuang sampah sembarangan adalah?",
        "Sampah B3 adalah sampah apa?",
        "Sampah kertas termasuk sampah apa?",
        "Sampah daun yang dikomposkan bisa menjadi?"
    ]
    jawaban_list = [
        "Anorganik",
        ["Termasuk","Iya"],
        ["Bisa Diurai", "Mudah Diurai"],
        "Komposting",
        ["Reduce Reuse Recycle", "Reduce, Reuse, Recycle"],
        ["Lingkungan Kotor", "banjir"],
        ["Beracun", "Berbahaya"],
        "Organik",
        "Pupuk"
        ]
    rndm = random.randint(0,(len(pertanyaan_list) - 1))
    pertanyaan = pertanyaan_list[rndm]
    jawaban = jawaban_list[rndm]
    await ctx.send(pertanyaan)
    msg = await bot.wait_for('message', check=check)
    client_jwb = msg.content.title().strip() # menghilangkan semua whitespace dan apapun yang bukan string 
    if isinstance(jawaban, list):
        if any(answer in client_jwb for answer in jawaban): # answer sebagai berbagai jawaban yang ada di var jawaban dan cek apakah ada answer di dalam jawaban client
            await ctx.send("Kamu benar!")
        else:
            result = "Kamu salah! Jawaban yang benar adalah: "
            for i in range(len(jawaban)):
                if i == 0:
                    result += jawaban[i]
                else:
                    result = result + ", " + jawaban[i]
            await ctx.send(result)
    else:
        if client_jwb in jawaban:
            await ctx.send("Kamu benar!")
        else:
            await ctx.send(f"Kamu salah! Jawaban yang benar adalah: {jawaban}")

@bot.command()
async def all_cmds(ctx):
    cmds = ("$hello: Bot menyapa anda.",
            "$hitung: Bot akan menghitung 2 angka yang disediakan client.",
            f"$assign: Bot akan memasukkan anda ke role {theRole}.",
            f"$remove: Bot akan menghapuskan anda dari role {theRole}.",
            "$dm msg: Bot akan dm anda dari pesan yang anda masukkan.",
            "$make_pass: Bot akan generate password random dengan panjang yang diinginkan oleh client.",
            "$tips: Bot akan memberikan tips untuk mengolah sampah anda",
            "$question: Bot akan menanyakan anda pertanyaan tentang sampah.",
            "$check: Bot akan mengidentifikasi jenis sampah yang anda berikan kepada bot.")
    for cmd in cmds:
        await ctx.send(cmd)



@bot.command()
async def check(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    async def getphoto(phoname):
        for pic in phoname:
            thePic = discord.File(pic) # menconvert path jadi file yang bisa diakses oleh discord
            await ctx.send(file=thePic)
    await ctx.send("Berikan kami foto sampahnya(sampah kertas, sampah plastik, botol plastik, sampah kaca, ban bekas, sampah rokok, dan sampah kaleng)")
    msg = await bot.wait_for('message', check=check) # check=check ngecek apakah file tersebut dikirim oleh pengguna yang memulai perintah ini serta ngecek channel sama atau tidak
        # kode untuk bot menerima gambar
    if msg.attachments:
        await ctx.send("Sedang kami klasifikasi, harap tunggu...") 
        for file in msg.attachments:
            print()
            await file.save(f'./temp_pictures/{file.filename}')
            hasil = get_class(model_path=f'./Misc/keras_model.h5', labels_path=f'./Misc/labels.txt', image_path=f'./temp_pictures/{file.filename}')
            folder_path = f"./temp_pictures"
            try:
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename) # Menggabungkan path folder dan file(dari ./temp_pictures & x.png menjadi ./temp_pictures/x.png)
                    if os.path.isfile(file_path):
                        os.remove(file_path) # Di hapus gambar setelah dicek sama model
                        print(f"{file_path} telah terhapus.")
            except:
                print("file not found/error")
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'plastik\n' and hasil[1] >= 0.65: #\n seperti tombol enter, turun kebawah 1 kali
                await ctx.send('Ini adalah sampah plastik')
                await ctx.send('Sampah plastik termasuk dalam kategori sampah anorganik karena sifatnya yang tidak mudah membusuk, tahan lama, ' \
                                'dan tidak dapat diurai dengan mudah oleh mikroorganisme di tanah')
                await ctx.send('Sampah plastik bisa di daur ulang untuk menjadi berbagai macam barang seperti celengan, botol baru, juga bisa menjadi furnitur')
                await ctx.send('Inilah beberapa gambar karya dari sampah plastik:')
                await getphoto(plastik)

            elif hasil[0] == 'kaleng\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah kaleng')
                await ctx.send('Sampah kaleng merupakan sampah anorganik, karena terbuat dari bahan logam dan tidak dapat terurai secara alami oleh mikroorganisme tanah')
                await ctx.send('Sampah kaleng bisa di daur ulang sebagai produk baru, contohnya membuat kaleng baru, vas bunga atau pot tanaman, dan bisa juga menjadikan tempat alat tulis dirumah')
                await ctx.send('Inilah beberapa gambar karya dari sampah kaleng:')
                await getphoto(kaleng)

            elif hasil[0] == 'kaca\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah kaca')
                await ctx.send('Sampah kaca termasuk jenis sampah anorganik karena sulit terurai oleh mikroorganisme yang disebabkan oleh bahan pembuatan.' \
                                'Bahannya berupa pasir silika, soda abu, dan batu kapur, bukan dari sisa-sisa makhluk hidup')
                await ctx.send('Tetapi sampah ini bisa di daur ulang dan akan menjadi lebih indah, beberapanya ada vas bunga, tempat lilin, dan kap lampu; hiasan dan dekorasi ' \
                                 'seperti mozaik kaca, lampu hias, dan figur miniatur')
                await ctx.send('Inilah beberapa gambar karya dari sampah kaca:')
                await getphoto(kaca)

            elif hasil[0] == 'botol plastik\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah botol plastik')
                await ctx.send('Sampah botol plastik merupakan jenis sampah anorganik dan memiliki karakteristik yang mirip dengan sampah plastik yaitu sulit diurai')
                await ctx.send('Tetapi sampah ini bisa di daur ulang menjadi kerajinan yang kreatif mulai dari pot bunga, celengan, tempat pensil, ' \
                                'wadah penyimpanan, hingga lampu hias dan hiasan dinding')
                await ctx.send('Inilah beberapa gambar karya dari sampah botol plastik:')
                await getphoto(botol)

            elif hasil[0] == 'kertas\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah kertas')
                await ctx.send('Sampah kertas merupakan sampah organik, tetapi merupakan jenis organik yang tidak mudah membusuk. ' \
                                'Meskipun terbuat dari bahan alami, sampah kertas dapat didaur ulang dengan waktu terurai yang bervariasi tergantung bahan')
                await ctx.send('Tetapi sampah ini bisa di daur ulang menjadi kertas baru atau menjadi kerajinan seperti vas bunga, tempat pensil, ' \
                                'keranjang, jam dinding, tas, hingga paper bag')
                await ctx.send('Inilah beberapa gambar karya dari sampah kertas:')
                await getphoto(kertas)

            elif hasil[0] == 'kardus\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah kardus')
                await ctx.send('Sampah kardus termasuk dalam kategori sampah anorganik karena bisa terurai secara alami ' \
                                'Kardus terbuat dari kertas atau karton yang secara alami bisa terurai, namun membutuhkan waktu yang lebih lama daripada sisa makanan')
                await ctx.send('Tetapi sampah ini bisa di daur ulang untuk membuat kardus baru atau membuat kerajinan tangan, contohnya seperti mainan anak, celengan, dan kotak tisu')
                await ctx.send('Inilah beberapa gambar karya dari sampah kardus:')
                await getphoto(kardus)

            elif hasil[0] == 'ban\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah ban')
                await ctx.send('Ban bekas termasuk sampah anorganik yang sangat sulit terurai dan dapat dikategorikan sebagai limbah B3 (Bahan Berbahaya dan Beracun) karena potensi risiko kebakaran, ' \
                                'emisi beracun, serta dampak buruk bagi kesehatan dan lingkungan jika tidak dikelola dengan baik.')
                await ctx.send('Tetapi sampah ini bisa di daur ulang menjadi ban baru atau bisa dibikin barang baru seperti kursi, pot bunga, hingga replika hewan')
                await ctx.send('Inilah beberapa gambar karya dari sampah ban:')
                await getphoto(ban)

            elif hasil[0] == 'rokok\n' and hasil[1] >= 0.65:
                await ctx.send('Ini adalah sampah rokok')
                await ctx.send('Sampah rokok adalah termasuk dalam kategori limbah B3 (Bahan Berbahaya dan Beracun) karena puntungnya mengandung mikroplastik, logam berat, dan zat kimia berbahaya yang dapat mencemari lingkungan serta membahayakan kesehatan, ' \
                                'tumbuhan, dan hewan, dan termasuk sampah anorganik yang sulit terurai secara alami. ')
                await ctx.send('Sampah ini tidak bisa di daur ulang karena mengandung zat beracun seperti nikotin, arsenik, timbal, dan masih ada 6000+ zat kimia berbahaya lainnya')
                await ctx.send('Rokok juga bisa menyebabkan banyak penyakit serius, seperti penyakit paru-paru (bronkitis kronis, emfisema, PPOK), kanker (paru-paru, mulut, tenggorokan, kerongkongan, lambung, pankreas, kandung kemih), penyakit jantung dan pembuluh darah (penyakit jantung koroner, ' \
                                'stroke, tekanan darah tinggi), serta gangguan sistem pencernaan (tukak lambung, refluks asam). Selain itu, merokok juga dapat merusak gigi dan gusi, menyebabkan gangguan pernapasan, dan membahayakan kehamilan, termasuk meningkatkan risiko komplikasi dan cacat lahir pada bayi. ')
            else:
                await ctx.send('Gambarmu kurang jelas')
                await ctx.send('Kirim gambar yang baru')
    else:
        await msg.delete()
        await ctx.send(f'{ctx.author.mention} filenya nggak bener >:( .  KIRIM LAGI')


bot.run("TOKEN")
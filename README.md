# Plesir Recommendation System  REST API 

## GET ALL TRAVEL 

### 

GET  http://127.0.0.1:8000/destinations/

```json
 "destination": [
        {
            "id": 1,
            "place_name": "Monumen Nasional",
            "description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat.",
            "category": "Budaya",
            "city": "Jakarta",
            "price": 20000.0,
            "hour": 0,
            "rating": 46
        }
]
```

## GET DETAIL TRAVEL AND SIMILAR ITEMS



GET  http://127.0.0.1:8000/destination/{id}/

```json
 "destination": {
        "id": 1,
        "place_name": "Monumen Nasional",
        "description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat.",
        "category": "Budaya",
        "city": "Jakarta",
        "price": 20000.0,
        "hour": 0,
        "rating": 46
    },
    "recommendations": [
        {
            "id": 259,
            "place_name": "Monumen Perjuangan Rakyat Jawa Barat",
            "description": "Monumen Perjuangan Rakyat Jawa Barat (Monju) adalah Museum Sejarah Perjuangan Rakyat Jawa Barat, di Tatar Pasundan atau Parahyangan. Monumen diresmikan oleh Gubernur Jawa Barat, Raden Nana Nuriana pada tanggal 23 Agustus 1995.",
            "category": "Budaya",
            "city": "Bandung",
            "price": 0.0,
            "hour": 0,
            "rating": 45
        },
```
 


## GET Destinations List (Using Pagination)

### Example in this documentation will be used 3 as limit and 0 for offset page (N-1)
GET  http://127.0.0.1:8000/destpaginated/?limit=3&offset=0

```json

{
    "count": 437,
    "next": "http://127.0.0.1:8000/destpaginated/?limit=3&offset=3",
    "previous": null,
    "results": [
        {
            "id": 1,
            "place_name": "Monumen Nasional",
            "description": "Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter (433 kaki) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat.",
            "category": "Budaya",
            "city": "Jakarta",
            "price": 20000.0,
            "hour": 0,
            "rating": 46
        },
        {
            "id": 2,
            "place_name": "Kota Tua",
            "description": "Kota tua di Jakarta, yang juga bernama Kota Tua, berpusat di Alun-Alun Fatahillah, yaitu alun-alun yang ramai dengan pertunjukan rutin tarian tradisional. Museum Sejarah Jakarta adalah bangunan era Belanda dengan lukisan dan barang antik, sedangkan Museum Wayang memamerkan boneka kayu khas Jawa. Desa Glodok, atau Chinatown, terkenal dengan makanan kaki lima, seperti pangsit dan mi goreng. Di dekatnya, terdapat sekunar dan kapal penangkap ikan di pelabuhan Sunda Kelapa yang kuno",
            "category": "Budaya",
            "city": "Jakarta",
            "price": 0.0,
            "hour": 1,
            "rating": 46
        },
        {
            "id": 3,
            "place_name": "Dunia Fantasi",
            "description": "Dunia Fantasi atau disebut juga Dufan adalah tempat hiburan yang terletak di kawasan Taman Impian Jaya Ancol, Jakarta Utara, Indonesia. Dufan diresmikan dan dibuka pada tanggal 29 Agustus 1985.",
            "category": "Taman Hiburan",
            "city": "Jakarta",
            "price": 270000.0,
            "hour": 6,
            "rating": 46
        }
    ]
}
```

## GET Search Destination by Name


GET  http://127.0.0.1:8000/search/?query=jogja

```json

{
    "Destination": [
        {
            "id": 89,
            "place_name": "De Mata Museum Jogja",
            "description": "Museum De Mata merupakan salah satu museum yang berisi lukisan 3D terbanyak di dunia. Jumlah lukisannya sekitar 120 dan setiap lukisan memiliki konsep dengan latar belakang yang terlihat seperti nyata. Ada beberapa ukuran lukisan yang ada di Museum De Mata dari ukuran biasa sampai mencapai 5 meter. Ada beberapa macam kategori lukisannya yaitu ornament, lanscape, olahraga, tokoh-tokoh terkenal, superhero, sampai lukisan sirkus. Museum ini didirikan untuk masyarakat menghabiskan liburan dengan menambah pengetahuan. Museum ini menawarkan banyak lukisan-lukisan yang unik misalnya terdapat lukisan dimana anda dapat merasakan keseruan berjalan di atas jembatan kayu yang dibawahnya terdapat jurang yang curam Atau berjuang untuk memadamkan semburanapi panas ari mulut naga, lukisan tersebut tampak seolah-olah nyata. Semua itu terdapat di dalam museum De Mata dengan hasil efek yang menipu mata.",
            "category": "Budaya",
            "city": "Yogyakarta",
            "price": 50000.0,
            "hour": 34,
            "rating": 44
        },
        {
            "id": 95,
            "place_name": "Desa Wisata Sungai Code Jogja Kota",
            "description": "Kampung Code berada di Kelurahan Kotabaru, Kecamatan Gondokusuman Kota Yogyakarta. Lokasi persisnya ada di RT 01/RW 01 di sebelah selatan jembatan Gondolayu di Jl Jenderal Sudirman atau di sebelah timur bantaran Kali Code yang membelah Kota Yogyakarta. Kampung Code terletak persis di bantaran Kali Code yang memanjang ke arah selatan dengan kontur tanah bertebing dari atas ke bawah. Di bagian atas yang mepet Jl Faridan M. Noto sebagian besar digunakan warga untuk usaha jasa/jual beli ban mobil. Sedangkan di bagian bawah menjadi tempat pemukiman warga. Kampung Code yang tadinya kampung biasa, menjelma menjadi sebuah karya seni berkat jasa seorang arsitek sekaligus pemuka agama katolik, Romo YB Manguwijaya.",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 0.0,
            "hour": 34,
            "rating": 5
        },
        {
            "id": 103,
            "place_name": "Tugu Pal Putih Jogja",
            "description": "Tugu Yogyakarta (Jawa: , Tugu Ngayogyakarta) adalah sebuah landmark bersejarah yang penting di kota Yogyakarta, Indonesia. Tugu berarti tugu, yang biasanya dibangun sebagai simbol suatu kawasan yang mengkonseptualisasikan ciri-ciri kawasan tersebut. Karena latar belakang sejarahnya, Tugu Yogyakarta telah menjadi ikon sejarah kota. Tugu Yogyakarta terletak tepat di tengah persimpangan antara Jalan Mangkubumi, Jalan Sudirman, Jalan A.M Sangaji, dan Jalan Dipenogoro kota._x000D_",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 0.0,
            "hour": 0,
            "rating": 47
        },
        {
            "id": 127,
            "place_name": "Blue Lagoon Jogja",
            "description": "Blue Lagoon adalah salah satu wisata air Jogja yang sudah sangat terkenal dan banyak dikunjungi oleh wisatawan dari berbagai daerah penjuru. Banyak yang menganggap bahwa Blue Lagoon sebagai surga wisata Jogja tersembunyi. Meskipun keindahan yang ditawarkan oleh tempat ini sangat mahal, namun untuk bisa menikmatinya kamu tidak perlu merogoh kocek dalam2. Karena budget untuk masuk ke area wisata ini tidak semahal yang ada di Islandia.",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 10000.0,
            "hour": 34,
            "rating": 43
        },
        {
            "id": 138,
            "place_name": "Jogja Exotarium",
            "description": "Di Yogyakarta, tepatnya di Sleman, ada satu tempat wisata edukasi yang patut dikunjungi. Namanya adalah Jogja Exotarium — terdengar unik, kan? Namun sebenarnya, tempat ini merupakan taman hewan berskala kecil. Koleksi hewannya beragam dan bisa diajak berinteraksi secara langsung",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 20000.0,
            "hour": 2,
            "rating": 44
        },
        {
            "id": 150,
            "place_name": "Wisata Kraton Jogja",
            "description": "Kraton Jogja adalah sebuah komplek kerajaan yang berada tepat berdiri di tengah kota Yogyakarta. Kraton yang didirikan seiring perjanjian giyanti pada tahun 1755 yang memecah Kerajaan Mataram Islam menjadi Kerajaan Ngayogyakarta Surakarta ini menyimpan keindahan arsitektur jawa yang tidak diragukan lagi, dan merupakan salah komplek istana terbaik di tanah jawa. Keindahan Kraton Jogja ini tidak terlepas dari pendirinya, yaitu Sri Sultan Hamengkubuwono I yang merupakan arsitek dari kerajaannya ini. Apabila anda sedang wisata ke Kraton Jogja maka apabila anda dari Jalan Malioboro pertama anda akan disambut oleh Gapura Pangurakan yang berasitrektur jawa kental yang bersebelahan dengan bangunan-bangunan Hindia Belanda. Setelah memasukinya anda akan memasuki Alun-alun Utara yang memiliki area yang cukup luas. Di sekelilingnya terdapat Joglo-joglo tertutup yang disebut Gedhong dan terbuka yang dinamakan Tratag. Di area ini terdapat beberapa pilihan kuliner yang sangat pas anda kunjungi sebelum anda memasuki kompleks Kraton Yogyakarta, sehingga anda tidak merasa kelaparan.",
            "category": "Budaya",
            "city": "Yogyakarta",
            "price": 7000.0,
            "hour": 34,
            "rating": 47
        },
        {
            "id": 180,
            "place_name": "Pantai Depok Jogja",
            "description": "Pantai Depok (bahasa Jawa: ꦥꦱꦶꦱꦶꦂ ꦝꦺꦥꦺꦴꦏ꧀, translit. Pasisir Dhépok) merupakan objek wisata pantai yang terletak di Kecamatan Kretek, Kabupaten Bantul, Daerah Istimewa Yogyakarta, sekitar tiga puluh kilometer di sebelah selatan Kota Yogyakarta. Pantai ini terkenal akan pasar ikannya yang ikannya merupakan hasil tangkapan nelayan Pantai Depok.",
            "category": "Bahari",
            "city": "Yogyakarta",
            "price": 10000.0,
            "hour": 34,
            "rating": 43
        },
        {
            "id": 183,
            "place_name": "Jogja Bay Pirates Adventure Waterpark",
            "description": "Jogja Bay Waterpark atau Jogja Bay (bahasa Jawa: ꦠꦼꦭꦸꦏ꧀ꦔꦪꦺꦴꦒꦾ 'Teluk Ngayogya') adalah salah satu taman wisata air atau waterpark terbesar di Asia Tenggara yang berlokasi di Yogyakarta, Indonesia. Taman wisata air ini dibuka secara resmi pada 20 Desember 2015.",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 150000.0,
            "hour": 34,
            "rating": 44
        },
        {
            "id": 203,
            "place_name": "Galaxy Waterpark Jogja",
            "description": "Galaxy Waterpark adalah taman rekreasi air yang berdiri di atas lahan seluas 2,5 hektar ini sangat cukup untuk menampung pengunjung di waktu liburan. Dengan lokasi yang sangat luas banyak wahana dan fasilitas yang bisa kamu nikmati. Di tempat ini juga tersedia beberapa kolam, dari kolam anak sampai kolam dewasa. Selain itu fasilitas yang disediakan pengelolapun juga terbilang lengkap untuk mendukung kenyamananmu saat berlibur.",
            "category": "Taman Hiburan",
            "city": "Yogyakarta",
            "price": 40000.0,
            "hour": 34,
            "rating": 43
        }
    ]
}
```
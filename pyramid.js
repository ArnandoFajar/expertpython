function pyramid(baris) {
  let hasil = "";

  for (let i = baris; i >= 1; i--) {
    // Tambahkan spasi sebelum bintang
    let spasi = "";
    for (let j = 1; j <= baris - i; j++) {
      spasi += " ";
    }

    // Tambahkan bintang
    let bintang = "";
    for (let k = 1; k <= i; k++) {
      bintang += "*";
    }

    // Gabungkan spasi dan bintang
    hasil += spasi + bintang;

    // Pindah ke baris baru
    hasil += "\n";
  }

  return hasil;
}

const baris = 5;
const result = pyramid(baris);
console.log(result);

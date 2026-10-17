import Quran

# Test 1: Temiz kelime sorgusu
harammihelalmi1 = "gambling"
Quran.checkHaram(harammihelalmi1)

# Test 2: Türkçe kelime sorgusu
Quran.checkHaram("kumar")

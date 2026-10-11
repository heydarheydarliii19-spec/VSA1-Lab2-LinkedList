**Tələbənin adı və soyadı:** Heydər Heydərli

**Qrup nömrəsi:** KOM25

**Laboratoriya işinin adı:** Singly Linked List-in reallaşdırılması və tətbiqi

## Yerinə yetirilmiş tapşırıqların siyahısı:

- Node sinfinin yaradılması
- Siyahının sonuna element əlavə edilməsi
- Siyahının əvvəlinə element əlavə edilməsi
- Verilmiş elementdən sonra əlavə etmə
- Element silmə
- Axtarış
- Uzunluğun hesablanması
- Maksimum və minimum element
- Siyahını tərs çevirmək
- Challenge
- Singly Linked List və Doubly Linked List müqayisəsi
 
## Proqramın iş prinsipi:
Bu proqramda Singly Linked List adi massiv yerinə düyünlərdən, yəni Node istifadə edilərək  qurulub. Hər düyündə iki şey saxlanılır: data-dəyər və next-növbəti düyünün ünvanı. Sonuncu düyünün next-i None olur, yəni siyahı bitir. Proqram yalnız birinci düyünü  tanıyır. Siyahının istənilən yerinə
çatmaq üçün head-dən başlayıb next vasitəsilə düyünləri ardıcıl keçirik. Axtarış, uzunluğun hesablanması, maksimum və minimum elementin tapılması məsələn, bu üsulla işləyir. Əlavə etmə və silmə zamanı elementləri sürüşdürmürük, sadəcə düyünlərin
next istinadlarını dəyişirik. Məsələn, ortadakı elementi silmək üçün ondan əvvəlki düyünün next-ini siləndən sonrakı düyünə yönəldirik. Siyahını tərsinə çevirəndə isə yeni siyahı yaratmırıq, mövcud düyünlərin next istiqamətini əksinə çeviririk.

## İcra təlimatı:
python linkedlist.py 

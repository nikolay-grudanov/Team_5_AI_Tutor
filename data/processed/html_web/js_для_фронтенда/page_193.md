---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.42
tokens: 6216
characters: 1368
timestamp: 2025-12-24T10:06:34.360917
finish_reason: stop
---

) || die "Неправильные параметры!\n";;
my $src_files = ();
find(\&all_src_files, @src_dir);
find(\&all_tested_files, $test_dir);

Мы принимаем параметры командной строки, "проходимся" по всем каталогам с исходным кодом и извлекаем имена всех JavaScript-файлов:

sub all_src_files {
    return unless (/\js$/);
    foreach my $src_dir (@src_dir) {
        $File::Find::name =~ s/^\Q$src_base\E//;
    }
    $src_files->{$File::Find::name}++;
}

Теперь хэш %src_files содержит все ваши JavaScript-файлы с исходным кодом. Далее приведен код для «прохода» по файлам тестов:

sub all_tested_files {
    return unless (/\html?$/);
    open(F, $_) || die "Can't open $_: $!\n";
    while(my $line = <F>) {
        if ($line =~ /["']([^\"]+)?V($src_keyV[^\"]+?\js))["']/) {
            my($full_file_path) = $2;
            print "Файл теста $File::Find::name покрыт $full_file_path\n" if ($debug);
            delete $src_files->{$full_file_path};
        }
    }
}

Самой неприятной вещью здесь, безусловно, является regex-поиск тегов сценария вида:

<script src="/path/to/JS/file"></script>

Как только имя файла будет удалено из хэша %src_files, оно будет помечено как «покрытое».

После этого хэш %src_files содержит только JavaScript-файлы без соответствующих тестов. Теперь очень просто использовать какую-либо систему шаблонов для создания пустого теста для каждого из
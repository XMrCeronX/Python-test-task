import unittest

from bs4 import BeautifulSoup
from solution import count_letter_group, parse_page, URL


class TestSolution2(unittest.TestCase):
    def setUp(self) -> None:
        self.letters = {}
        self.bf = BeautifulSoup(
            """
            <div id="mw-pages">
            <h2>Страницы в категории «Животные по алфавиту»</h2>
            <p>Показано 200 страниц из 46&nbsp;286, находящихся в данной категории. <a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/FAQ#Страница_категории_не_обновляется" title="Википедия:Категоризация/FAQ">Список ниже может не отражать последних изменений.</a>
            </p>
            <div style="font-size:85%; padding:0.1412em 0;">Инструменты:
            <style data-mw-deduplicate="TemplateStyles:r136833263">.mw-parser-output .hlist dl,.mw-parser-output .hlist.hlist ol,.mw-parser-output .hlist.hlist ul{margin:0;padding:0}.mw-parser-output .hlist dd,.mw-parser-output .hlist dt,.mw-parser-output .hlist li{margin:0;display:inline}.mw-parser-output .hlist.inline,.mw-parser-output .hlist.inline dl,.mw-parser-output .hlist.inline ol,.mw-parser-output .hlist.inline ul,.mw-parser-output .hlist dl dl,.mw-parser-output .hlist dl ol,.mw-parser-output .hlist dl ul,.mw-parser-output .hlist ol dl,.mw-parser-output .hlist ol ol,.mw-parser-output .hlist ol ul,.mw-parser-output .hlist ul dl,.mw-parser-output .hlist ul ol,.mw-parser-output .hlist ul ul{display:inline}.mw-parser-output .hlist .mw-empty-li,.mw-parser-output .hlist .mw-empty-elt{display:none}.mw-parser-output .hlist dt:after{content:": "}.mw-parser-output .hlist dd:after,.mw-parser-output .hlist li:after{content:"\a0 · ";font-weight:bold}.mw-parser-output .hlist dd:last-child:after,.mw-parser-output .hlist dt:last-child:after,.mw-parser-output .hlist li:last-child:after{content:none}.mw-parser-output .hlist dd dd:first-child:before,.mw-parser-output .hlist dd dt:first-child:before,.mw-parser-output .hlist dd li:first-child:before,.mw-parser-output .hlist dt dd:first-child:before,.mw-parser-output .hlist dt dt:first-child:before,.mw-parser-output .hlist dt li:first-child:before,.mw-parser-output .hlist li dd:first-child:before,.mw-parser-output .hlist li dt:first-child:before,.mw-parser-output .hlist li li:first-child:before{content:" (";font-weight:normal}.mw-parser-output .hlist dd dd:last-child:after,.mw-parser-output .hlist dd dt:last-child:after,.mw-parser-output .hlist dd li:last-child:after,.mw-parser-output .hlist dt dd:last-child:after,.mw-parser-output .hlist dt dt:last-child:after,.mw-parser-output .hlist dt li:last-child:after,.mw-parser-output .hlist li dd:last-child:after,.mw-parser-output .hlist li dt:last-child:after,.mw-parser-output .hlist li li:last-child:after{content:")";font-weight:normal}.mw-parser-output .hlist ol{counter-reset:listitem}.mw-parser-output .hlist ol>li{counter-increment:listitem}.mw-parser-output .hlist ol>li:before{content:" "counter(listitem)"\a0 "}.mw-parser-output .hlist dd ol>li:first-child:before,.mw-parser-output .hlist dt ol>li:first-child:before,.mw-parser-output .hlist li ol>li:first-child:before{content:" ("counter(listitem)"\a0 "}.mw-parser-output .hlist-items-nowrap dd,.mw-parser-output .hlist-items-nowrap dt,.mw-parser-output .hlist-items-nowrap li{white-space:nowrap}.mw-parser-output .hlist-items-nowrap dl dl,.mw-parser-output .hlist-items-nowrap dl ol,.mw-parser-output .hlist-items-nowrap dl ul,.mw-parser-output .hlist-items-nowrap ol dl,.mw-parser-output .hlist-items-nowrap ol ol,.mw-parser-output .hlist-items-nowrap ol ul,.mw-parser-output .hlist-items-nowrap ul dl,.mw-parser-output .hlist-items-nowrap ul ol,.mw-parser-output .hlist-items-nowrap ul ul{white-space:normal}</style><div class="hlist inline plainlinks" style="margin-left: 0em;">
            <ul><li><a rel="nofollow" class="external text" href="https://petscan.wmflabs.org/?language=ru&amp;project=wikipedia&amp;depth=3&amp;categories=%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp;interface_language=ru">PetScan</a></li>
            <li><a class="external text" href="https://vcat.toolforge.org/render?wiki=ruwiki&amp;category=%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83">Дерево категорий</a></li>
            <li><a href="/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:RandomInCategory/%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83" title="Служебная:RandomInCategory/Животные по алфавиту">Случайная страница в категории</a></li></ul>
            </div></div>(<a href="/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp;filefrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;pageuntil=%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D1%82%D1%80%D0%BE%D0%B3%D0%BE%D0%BD%D1%8B&amp;subcatfrom=%3Cb%3E%D0%AF%3C%2Fb%3E#mw-pages" title="Категория:Животные по алфавиту">Предыдущая страница</a>) (<a href="/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp;filefrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;subcatfrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;pagefrom=%D0%91%D0%B0%D1%80%D1%81%D1%83%D0%BA#mw-pages" title="Категория:Животные по алфавиту">Следующая страница</a>)<div lang="ru" dir="ltr" class="mw-content-ltr"><div class="mw-category mw-category-columns"><div class="mw-category-group"><h3>А</h3>
            <ul><li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D1%82%D1%80%D0%BE%D0%B3%D0%BE%D0%BD%D1%8B" title="Африканские трогоны">Африканские трогоны</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D1%83%D0%B7%D0%BA%D0%BE%D1%80%D0%BE%D1%82%D1%8B" title="Африканские узкороты">Африканские узкороты</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D1%87%D0%B5%D1%85%D0%BE%D0%BD%D0%B8" title="Африканские чехони">Африканские чехони</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D1%8F%D0%B8%D1%87%D0%BD%D1%8B%D0%B5_%D0%B7%D0%BC%D0%B5%D0%B8" title="Африканские яичные змеи">Африканские яичные змеи</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%BB%D0%BE%D0%BF%D0%B8%D1%82%D0%B5%D0%BA" title="Африканский австралопитек">Африканский австралопитек</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%B8%D1%81%D1%82-%D1%80%D0%B0%D0%B7%D0%B8%D0%BD%D1%8F" title="Африканский аист-разиня">Африканский аист-разиня</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D0%B5%D0%BB%D0%BE%D0%B3%D0%BE%D1%80%D0%BB%D1%8B%D0%B9_%D0%B3%D1%80%D0%B8%D1%84" title="Африканский белогорлый гриф">Африканский белогорлый гриф</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D0%B5%D0%BB%D0%BE%D1%85%D0%BE%D1%85%D0%BB%D1%8B%D0%B9_%D0%BA%D0%B0%D0%BB%D0%B0%D0%BE" title="Африканский белохохлый калао">Африканский белохохлый калао</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D0%BB%D0%B5%D1%81%D1%82%D1%8F%D1%89%D0%B8%D0%B9_%D1%87%D0%B8%D1%80%D0%BE%D0%BA" title="Африканский блестящий чирок">Африканский блестящий чирок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B5%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BC%D1%83%D1%80%D0%B0%D0%B2%D0%B5%D0%B9" title="Африканский большеголовый муравей">Африканский большеголовый муравей</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D1%83%D0%B9%D0%B2%D0%BE%D0%BB" title="Африканский буйвол">Африканский буйвол</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%B5%D0%B7" title="Африканский водорез">Африканский водорез</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BB%D1%87%D0%B8%D0%B9_%D1%88%D0%B0%D0%BA%D0%B0%D0%BB" title="Африканский волчий шакал">Африканский волчий шакал</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D1%8B%D0%BC%D0%BF%D0%B5%D0%BB%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BA%D0%BE%D0%B7%D0%BE%D0%B4%D0%BE%D0%B9" title="Африканский вымпеловый козодой">Африканский вымпеловый козодой</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%B8%D0%B4%D1%80%D0%BE%D0%BB%D0%B0%D0%B3" title="Африканский гидролаг">Африканский гидролаг</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D0%BB%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82" title="Африканский голохвост">Африканский голохвост</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D1%80%D0%BD%D1%8B%D0%B9_%D0%BA%D0%B0%D0%BD%D1%8E%D0%BA" title="Африканский горный канюк">Африканский горный канюк</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D1%80%D0%B8%D1%84" title="Африканский гриф">Африканский гриф</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D1%83%D1%81%D1%8C" title="Африканский гусь">Африканский гусь</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B4%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B0%D0%B7" title="Африканский дикобраз">Африканский дикобраз</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B4%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82%D1%8B%D0%B9_%D1%8F%D1%81%D1%82%D1%80%D0%B5%D0%B1" title="Африканский длиннохвостый ястреб">Африканский длиннохвостый ястреб</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B4%D1%8B%D0%BC%D1%87%D0%B0%D1%82%D1%8B%D0%B9_%D0%BA%D0%BE%D1%80%D1%88%D1%83%D0%BD" title="Африканский дымчатый коршун">Африканский дымчатый коршун</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B4%D1%8F%D1%82%D0%B5%D0%BB%D0%BE%D0%BA" title="Африканский дятелок">Африканский дятелок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%B0%D1%8F%D1%86" title="Африканский заяц">Африканский заяц</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B7%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%BB%D1%83%D0%B1%D1%8C" title="Африканский зелёный голубь">Африканский зелёный голубь</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D1%80%D0%B0%D0%BD%D0%BA%D1%81" title="Африканский каранкс">Африканский каранкс</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D1%80%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BB%D0%B5%D1%81%D0%BD%D0%BE%D0%B9_%D0%B7%D0%B8%D0%BC%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%BA" title="Африканский карликовый лесной зимородок">Африканский карликовый лесной зимородок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%B0%D1%80%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D1%81%D0%BE%D0%BA%D0%BE%D0%BB" title="Африканский карликовый сокол">Африканский карликовый сокол</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BB%D0%B0%D1%80%D0%B8%D0%B5%D0%B2%D1%8B%D0%B9_%D1%81%D0%BE%D0%BC" title="Африканский клариевый сом">Африканский клариевый сом</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BB%D1%8E%D0%B2%D0%B0%D1%87" title="Африканский клювач">Африканский клювач</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D1%8C" title="Африканский коростель">Африканский коростель</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82%D1%8B%D0%B9_%D0%BA%D0%B0%D0%BD%D1%8E%D0%BA" title="Африканский краснохвостый канюк">Африканский краснохвостый канюк</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%BE%D1%88%D0%B5%D1%87%D0%BD%D1%8B%D0%B9_%D0%B7%D0%B8%D0%BC%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%BA" title="Африканский крошечный зимородок">Африканский крошечный зимородок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%83%D1%81%D1%82%D0%B0%D1%80%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D0%B6%D0%B0%D0%B2%D0%BE%D1%80%D0%BE%D0%BD%D0%BE%D0%BA" title="Африканский кустарниковый жаворонок">Африканский кустарниковый жаворонок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D0%B0%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D0%BD" title="Африканский ламантин">Африканский ламантин</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D0%B0%D0%BF%D1%87%D0%B0%D1%82%D0%BE%D0%BD%D0%BE%D0%B3" title="Африканский лапчатоног">Африканский лапчатоног</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D0%B5%D0%BE%D0%BF%D0%B0%D1%80%D0%B4" title="Африканский леопард">Африканский леопард</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D0%B8%D0%BD%D0%B7%D0%B0%D0%BD%D0%B3" title="Африканский линзанг">Африканский линзанг</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BB%D1%83%D0%BD%D1%91%D0%B2%D1%8B%D0%B9_%D1%8F%D1%81%D1%82%D1%80%D0%B5%D0%B1" title="Африканский лунёвый ястреб">Африканский лунёвый ястреб</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%B0%D0%BB%D1%8B%D0%B9_%D0%BF%D0%B5%D1%80%D0%B5%D0%BF%D0%B5%D0%BB%D1%8F%D1%82%D0%BD%D0%B8%D0%BA" title="Африканский малый перепелятник">Африканский малый перепелятник</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%B0%D1%80%D0%B0%D0%B1%D1%83" title="Африканский марабу">Африканский марабу</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%B5%D1%88%D0%BA%D0%BE%D0%BA%D1%80%D1%8B%D0%BB" title="Африканский мешкокрыл">Африканский мешкокрыл</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB" title="Африканский морской ангел">Африканский морской ангел</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B0%D0%B3%D1%80" title="Африканский пагр">Африканский пагр</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B8%D0%BB%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82" title="Африканский пилохвост">Африканский пилохвост</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D1%81%D0%B5%D1%82%D1%82%D0%BE%D0%B4" title="Африканский псеттод">Африканский псеттод</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D1%83%D1%88%D0%B8%D1%81%D1%82%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B3%D0%BE%D0%BD%D1%8B%D1%88" title="Африканский пушистый погоныш">Африканский пушистый погоныш</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B5%D1%80%D1%8B%D0%B9_%D1%82%D0%BE%D0%BA%D0%BE" title="Африканский серый токо">Африканский серый токо</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B8%D0%BF" title="Африканский сип">Африканский сип</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D1%82%D1%80%D0%B0%D1%83%D1%81" title="Африканский страус">Африканский страус</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D1%82%D0%B5%D1%80%D0%B5%D0%B2%D1%8F%D1%82%D0%BD%D0%B8%D0%BA" title="Африканский тетеревятник">Африканский тетеревятник</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D1%80%D0%B8%D0%BE%D0%BD%D0%B8%D0%BA%D1%81" title="Африканский трионикс">Африканский трионикс</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%83%D0%B4%D0%BE%D0%B4" title="Африканский удод">Африканский удод</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%83%D0%B7%D0%BA%D0%BE%D1%80%D1%8B%D0%BB%D1%8B%D0%B9_%D0%BA%D1%80%D0%BE%D0%BA%D0%BE%D0%B4%D0%B8%D0%BB" title="Африканский узкорылый крокодил">Африканский узкорылый крокодил</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%83%D1%88%D0%B0%D1%81%D1%82%D1%8B%D0%B9_%D0%B3%D1%80%D0%B8%D1%84" title="Африканский ушастый гриф">Африканский ушастый гриф</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%84%D0%B8%D0%BB%D0%B8%D0%BD" title="Африканский филин">Африканский филин</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%85%D0%BE%D1%80%D1%91%D0%BA" title="Африканский хорёк">Африканский хорёк</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%87%D0%B5%D0%B3%D0%BB%D0%BE%D0%BA" title="Африканский чеглок">Африканский чеглок</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%87%D1%91%D1%80%D0%BD%D1%8B%D0%B9_%D0%BA%D1%83%D0%BB%D0%B8%D0%BA-%D1%81%D0%BE%D1%80%D0%BE%D0%BA%D0%B0" title="Африканский чёрный кулик-сорока">Африканский чёрный кулик-сорока</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%88%D0%B5%D1%81%D1%82%D0%B8%D0%B6%D0%B0%D0%B1%D0%B5%D1%80%D0%BD%D1%8B%D0%B9_%D1%81%D0%BA%D0%B0%D1%82" title="Африканский шестижаберный скат">Африканский шестижаберный скат</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%88%D0%B8%D0%BF%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82" title="Африканский шипохвост">Африканский шипохвост</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%88%D0%B8%D1%80%D0%BE%D0%BA%D0%BE%D1%80%D0%BE%D1%82" title="Африканский широкорот">Африканский широкорот</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5_%D0%BB%D0%BE%D0%B6%D0%BD%D1%8B%D0%B5_%D0%B2%D0%B0%D0%BC%D0%BF%D0%B8%D1%80%D1%8B" title="Афроазиатские ложные вампиры">Афроазиатские ложные вампиры</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5_%D1%8F%D1%89%D1%83%D1%80%D0%BA%D0%B8" title="Афроазиатские ящурки">Афроазиатские ящурки</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D0%B0%D1%82%D0%BE%D1%80" title="Афровенатор">Афровенатор</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D0%B4%D0%B8%D1%82%D0%BE%D0%B2%D1%8B%D0%B5" title="Афродитовые">Афродитовые</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D0%BF%D0%B8%D1%82%D0%B5%D0%BA" title="Афропитек">Афропитек</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D1%81%D0%BE%D1%80%D0%B8%D1%86%D0%B8%D0%B4%D1%8B" title="Афросорициды">Афросорициды</a></li>
            <li><a href="/wiki/%D0%90%D1%84%D1%80%D0%BE%D1%82%D0%B5%D1%80%D0%B8%D0%B8" title="Афротерии">Афротерии</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B0%D1%82%D0%B8%D0%BD%D0%B0_%D0%B3%D0%B8%D0%B3%D0%B0%D0%BD%D1%82%D1%81%D0%BA%D0%B0%D1%8F" title="Ахатина гигантская">Ахатина гигантская</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B0%D1%82%D0%B8%D0%BD%D0%B5%D0%BB%D0%BB%D0%B8%D0%B4%D1%8B" title="Ахатинеллиды">Ахатинеллиды</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D0%B4%D1%8B" title="Ахатиниды">Ахатиниды</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B0%D1%82%D0%B8%D0%BD%D1%8B" title="Ахатины">Ахатины</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B5%D0%BB%D0%BE%D0%B7%D0%B0%D0%B2%D1%80" title="Ахелозавр">Ахелозавр</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B8%D0%BB%D0%B8%D0%B4%D1%8B" title="Ахилиды">Ахилиды</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B8%D0%BB%D0%BB%D0%B5%D0%B7%D0%B0%D0%B2%D1%80" title="Ахиллезавр">Ахиллезавр</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B8%D0%BB%D0%BB%D0%BE%D0%B1%D0%B0%D1%82%D0%BE%D1%80" title="Ахиллобатор">Ахиллобатор</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B8%D1%80%D0%BE%D0%B2%D1%8B%D0%B5" title="Ахировые">Ахировые</a></li>
            <li><a href="/wiki/%D0%90%D1%85%D0%B8%D1%80%D0%BE%D0%BF%D1%81%D0%B5%D1%82%D1%82%D0%BE%D0%B2%D1%8B%D0%B5" title="Ахиропсеттовые">Ахиропсеттовые</a></li>
            <li><a href="/wiki/%D0%90%D1%86%D0%B5%D0%BB%D0%BE%D0%BC%D0%BE%D1%80%D1%84%D1%8B" title="Ацеломорфы">Ацеломорфы</a></li>
            <li><a href="/wiki/%D0%90%D1%86%D0%B5%D1%80%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B8" title="Ацератерии">Ацератерии</a></li>
            <li><a href="/wiki/%D0%90%D1%86%D0%B5%D1%80%D0%BE%D0%B4%D0%BE%D0%BD_%D0%9C%D0%B0%D0%BA%D0%BB%D0%BE%D1%82%D0%B0" title="Ацеродон Маклота">Ацеродон Маклота</a></li>
            <li><a href="/wiki/%D0%90%D1%86%D0%B5%D1%80%D0%BE%D0%B4%D0%BE%D0%BD%D1%8B" title="Ацеродоны">Ацеродоны</a></li>
            <li><a href="/wiki/%D0%90%D1%86%D1%82%D0%B5%D0%BA%D1%81%D0%BA%D0%B0%D1%8F_%D1%87%D0%B0%D0%B9%D0%BA%D0%B0" title="Ацтекская чайка">Ацтекская чайка</a></li>
            <li><a href="/wiki/%D0%90%D1%8D%D1%80%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BD" title="Аэростеон">Аэростеон</a></li>
            <li><a href="/wiki/%D0%90%D1%8E_(%D1%80%D1%8B%D0%B1%D0%B0)" title="Аю (рыба)">Аю (рыба)</a></li></ul></div><div class="mw-category-group"><h3>Б</h3>
            <ul><li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B0%D0%BA%D0%BE%D1%82%D0%B8%D0%B8" title="Бабакотии">Бабакотии</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B0%D0%BA%D1%81_%D0%9A%D0%BE%D0%B7%D0%BB%D0%BE%D0%B2%D0%B0" title="Бабакс Козлова">Бабакс Козлова</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B0%D0%BA%D1%81%D1%8B" title="Бабаксы">Бабаксы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B1%D0%BB%D0%B5%D1%80-%D0%BA%D0%B0%D0%BF%D1%83%D1%86%D0%B8%D0%BD" title="Бабблер-капуцин">Бабблер-капуцин</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B8%D1%80%D1%83%D1%81%D1%81%D0%B0" title="Бабирусса">Бабирусса</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%B8%D1%80%D1%83%D1%81%D1%81%D1%8B" title="Бабируссы">Бабируссы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B0_%D0%B0%D0%BB%D1%8C%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F" title="Бабка альпийская">Бабка альпийская</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B0_%D0%B0%D1%80%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F" title="Бабка арктическая">Бабка арктическая</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B0_%D0%B1%D1%80%D0%BE%D0%BD%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F" title="Бабка бронзовая">Бабка бронзовая</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B0_%D0%B6%D1%91%D0%BB%D1%82%D0%BE%D0%BF%D1%8F%D1%82%D0%BD%D0%B8%D1%81%D1%82%D0%B0%D1%8F" title="Бабка жёлтопятнистая">Бабка жёлтопятнистая</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B0_%D0%BC%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F" title="Бабка металлическая">Бабка металлическая</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B8_(%D0%BD%D0%B0%D1%81%D0%B5%D0%BA%D0%BE%D0%BC%D1%8B%D0%B5)" title="Бабки (насекомые)">Бабки (насекомые)</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BA%D0%B8_(%D1%80%D0%BE%D0%B4)" title="Бабки (род)">Бабки (род)</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%BA%D0%B0-%D0%BC%D0%BE%D0%BA%D1%80%D0%B8%D1%86%D0%B0" title="Бабочка-мокрица">Бабочка-мокрица</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%BA%D0%B0-%D0%BE%D1%81%D0%BB%D0%B8%D0%BA" title="Бабочка-ослик">Бабочка-ослик</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%BD%D0%B8%D0%BA_%D0%BE%D0%BF%D0%B0%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B9" title="Бабочник опалённый">Бабочник опалённый</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%BD%D0%B8%D1%86%D1%8B" title="Бабочницы">Бабочницы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B1%D1%83%D0%B8%D0%BD" title="Бабуин">Бабуин</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B2%D0%B0%D0%B9%D0%B8" title="Бавайи">Бавайи</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B2%D0%B0%D1%80%D0%B8%D0%B7%D0%B0%D0%B2%D1%80" title="Баваризавр">Баваризавр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B2%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%91%D0%B2%D0%BA%D0%B0" title="Баварская полёвка">Баварская полёвка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B0%D1%8F_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%BB%D0%B0%D1%81%D1%82%D0%BE%D1%87%D0%BA%D0%B0" title="Багамская американская ласточка">Багамская американская ласточка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B0%D1%8F_%D0%BA%D0%BE%D1%88%D0%B0%D1%87%D1%8C%D1%8F_%D0%B0%D0%BA%D1%83%D0%BB%D0%B0" title="Багамская кошачья акула">Багамская кошачья акула</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B0%D1%8F_%D1%82%D0%B0%D0%BD%D0%B0%D0%B3%D1%80%D0%B0" title="Багамская танагра">Багамская танагра</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B0%D1%8F_%D1%85%D1%83%D1%82%D0%B8%D1%8F" title="Багамская хутия">Багамская хутия</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B5_%D1%82%D0%B0%D0%BD%D0%B0%D0%B3%D1%80%D1%8B" title="Багамские танагры">Багамские танагры</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BB%D0%B0%D0%B4%D0%BA%D0%BE%D0%B3%D1%83%D0%B1%D1%8B%D0%B9_%D1%83%D0%B4%D0%B0%D0%B2" title="Багамский гладкогубый удав">Багамский гладкогубый удав</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%B5%D0%BD%D0%BE%D1%82" title="Багамский енот">Багамский енот</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D0%BD%D0%BE%D1%87%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BF%D0%B5%D0%B2%D1%83%D0%BD" title="Багамский пеночковый певун">Багамский пеночковый певун</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B8%D0%BB%D0%BE%D0%BD%D0%BE%D1%81" title="Багамский пилонос">Багамский пилонос</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D1%80%D0%B0%D0%B0%D1%82%D0%B0%D0%BD" title="Багараатан">Багараатан</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D1%80%D0%B8%D0%B5%D0%B2%D1%8B%D0%B5" title="Багариевые">Багариевые</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D1%80%D0%B8%D0%B8" title="Багарии">Багарии</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B3%D0%B0%D1%86%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D0%BF%D1%81" title="Багацератопс">Багацератопс</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B4%D1%8F%D0%B3%D0%B8" title="Бадяги">Бадяги</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B7%D0%B0%D1%80%D0%BD%D0%B0%D1%8F_%D0%BC%D1%83%D1%85%D0%B0" title="Базарная муха">Базарная муха</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B7%D0%B8%D0%BB%D0%BE%D0%B7%D0%B0%D0%B2%D1%80%D0%B8%D0%B4%D1%8B" title="Базилозавриды">Базилозавриды</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B7%D0%B8%D0%BB%D0%BE%D0%B7%D0%B0%D0%B2%D1%80%D1%8B" title="Базилозавры">Базилозавры</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B9%D0%B1%D0%B0%D0%BA" title="Байбак">Байбак</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B9%D0%B4%D0%B0%D0%B1%D0%B0%D1%82%D1%8B%D1%80" title="Байдабатыр">Байдабатыр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%BD%D0%B5%D1%80%D0%BF%D0%B0" title="Байкальская нерпа">Байкальская нерпа</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D1%8D%D0%BF%D0%B8%D1%88%D1%83%D1%80%D0%B0" title="Байкальская эпишура">Байкальская эпишура</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D0%BC%D1%83%D0%BB%D1%8C" title="Байкальский омуль">Байкальский омуль</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BA%D0%BB%D0%B0%D0%BD_%D0%91%D1%83%D0%B3%D0%B5%D0%BD%D0%B2%D0%B8%D0%BB%D1%8F" title="Баклан Бугенвиля">Баклан Бугенвиля</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BA%D0%BB%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5" title="Баклановые">Баклановые</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BA%D0%BB%D0%B0%D0%BD%D1%8B" title="Бакланы">Бакланы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BA%D0%BE%D0%BD%D0%B8%D0%B4%D1%80%D0%B0%D0%BA%D0%BE" title="Баконидрако">Баконидрако</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BA%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%B2%D1%80" title="Бактрозавр">Бактрозавр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B0%D0%BD%D0%BE%D0%B3%D0%BB%D0%BE%D1%81%D1%81" title="Баланоглосс">Баланоглосс</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B0%D1%83%D1%80_(%D0%B4%D0%B8%D0%BD%D0%BE%D0%B7%D0%B0%D0%B2%D1%80)" title="Балаур (динозавр)">Балаур (динозавр)</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%B6%D0%B0%D0%B1%D0%B0-%D0%BF%D0%BE%D0%B2%D0%B8%D1%82%D1%83%D1%85%D0%B0" title="Балеарская жаба-повитуха">Балеарская жаба-повитуха</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BB%D0%B0%D0%B2%D0%BA%D0%B0" title="Балеарская славка">Балеарская славка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D1%8F%D1%89%D0%B5%D1%80%D0%B8%D1%86%D0%B0" title="Балеарская ящерица">Балеарская ящерица</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B1%D1%83%D1%80%D0%B5%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D0%B8%D0%BA" title="Балеарский буревестник">Балеарский буревестник</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BE%D0%B7%D1%91%D0%BB" title="Балеарский козёл">Балеарский козёл</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B5%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%B1%D0%B5%D0%BB%D0%BE%D0%B7%D1%83%D0%B1%D0%BA%D0%B0" title="Балесская белозубка">Балесская белозубка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BA%D0%B2%D0%BE%D1%80%D0%B5%D1%86" title="Балийский скворец">Балийский скворец</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B8%D0%B3%D1%80" title="Балийский тигр">Балийский тигр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%B8%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D1%8B%D0%B5" title="Балиторовые">Балиторовые</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%91%D0%B2%D0%BA%D0%B0" title="Балканская полёвка">Балканская полёвка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%80%D1%8B%D1%81%D1%8C" title="Балканская рысь">Балканская рысь</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%87%D0%B5%D1%80%D0%B5%D0%BF%D0%B0%D1%85%D0%B0" title="Балканская черепаха">Балканская черепаха</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D0%BE%D0%B7" title="Балканский полоз">Балканский полоз</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D0%BE%D0%B1%D0%B0%D0%BD" title="Балобан">Балобан</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BA%D0%BE%D0%BB%D1%8C%D1%87%D0%B0%D1%82%D0%B0%D1%8F_%D0%BD%D0%B5%D1%80%D0%BF%D0%B0" title="Балтийская кольчатая нерпа">Балтийская кольчатая нерпа</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BC%D0%B0%D0%BA%D0%BE%D0%BC%D0%B0" title="Балтийская макома">Балтийская макома</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%B5%D1%81%D1%87%D0%B0%D0%BD%D0%BA%D0%B0" title="Балтийская песчанка">Балтийская песчанка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D1%89%D0%B8%D0%BF%D0%BE%D0%B2%D0%BA%D0%B0" title="Балтийская щиповка">Балтийская щиповка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%B8%D0%B2%D0%BE%D0%BB%D0%B3%D0%B0" title="Балтиморская иволга">Балтиморская иволга</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%85%D0%B0%D1%88%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BE%D1%80%D0%BD%D0%B5%D0%B5%D0%B4" title="Балхашский корнеед">Балхашский корнеед</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%85%D0%B0%D1%88%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D0%BA%D1%83%D0%BD%D1%8C" title="Балхашский окунь">Балхашский окунь</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BB%D1%8F%D0%BD%D1%83%D1%81%D1%8B" title="Балянусы">Балянусы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%B6%D0%B5%D0%BB%D1%82%D0%BE%D0%B1%D1%80%D1%8E%D1%85%D0%B0%D1%8F_%D0%BA%D0%B0%D0%BC%D1%8B%D1%88%D0%BE%D0%B2%D0%BA%D0%B0" title="Бамбуковая желтобрюхая камышовка">Бамбуковая желтобрюхая камышовка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D1%83%D1%80%D0%BE%D0%BF%D0%B0%D1%82%D0%BA%D0%B0" title="Бамбуковая куропатка">Бамбуковая куропатка</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D1%83%D1%84%D0%B8%D1%8F" title="Бамбуковая куфия">Бамбуковая куфия</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5_%D0%B4%D1%8F%D1%82%D0%BB%D1%8B" title="Бамбуковые дятлы">Бамбуковые дятлы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D0%B4%D1%8F%D1%82%D0%B5%D0%BB" title="Бамбуковый дятел">Бамбуковый дятел</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D1%82%D0%BE%D0%BF%D0%B0%D0%BA%D0%BE%D0%BB%D0%BE" title="Бамбуковый топаколо">Бамбуковый топаколо</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BC%D0%B1%D1%83%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D1%83%D0%B3%D0%BB%D0%BE%D0%B7%D1%83%D0%B1" title="Бамбуковый углозуб">Бамбуковый углозуб</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BD%D0%B8%D1%86%D1%8B" title="Бананницы">Бананницы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BB%D0%B8%D1%81%D1%82%D0%BE%D0%BD%D0%BE%D1%81" title="Банановый листонос">Банановый листонос</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BF%D0%B5%D0%B2%D1%83%D0%BD" title="Банановый певун">Банановый певун</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D1%81%D0%B2%D0%B5%D1%80%D1%87%D0%BE%D0%BA" title="Банановый сверчок">Банановый сверчок</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD%D0%BE%D0%B5%D0%B4%D1%8B-%D0%BF%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B6%D0%BD%D0%B8%D0%BA%D0%B8" title="Бананоеды-подорожники">Бананоеды-подорожники</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B3%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%B2%D0%BE%D1%80%D0%BE%D0%BD%D0%B0" title="Бангайская ворона">Бангайская ворона</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B4%D0%B8%D0%BA%D0%BE%D1%82%D1%8B" title="Бандикоты">Бандикоты</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B4%D0%B8%D0%BA%D1%83%D1%82%D0%BE%D0%B2%D1%8B%D0%B5" title="Бандикутовые">Бандикутовые</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%B4%D0%B8%D0%BA%D1%83%D1%82%D1%8B" title="Бандикуты">Бандикуты</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D0%BA%D0%B8%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%B4%D0%B6%D1%83%D0%BD%D0%B3%D0%BB%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B0" title="Банкивская джунглевая курица">Банкивская джунглевая курица</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D1%82%D0%B5%D0%BD%D0%B3" title="Бантенг">Бантенг</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D0%BD%D1%8C%D1%86%D0%B7%D0%B8" title="Баньцзи">Баньцзи</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%85%D0%BE%D0%BC%D1%8F%D1%87%D0%BE%D0%BA" title="Барабинский хомячок">Барабинский хомячок</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%B1%D1%83%D0%BB%D0%B5%D0%B2%D1%8B%D0%B5" title="Барабулевые">Барабулевые</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%B1%D1%83%D0%BB%D0%B8" title="Барабули">Барабули</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%BD_%D0%94%D0%B0%D0%BB%D0%BB%D0%B0" title="Баран Далла">Баран Далла</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%BD%D1%8B" title="Бараны">Бараны</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D0%BF%D0%B0%D0%B7%D0%B0%D0%B2%D1%80" title="Барапазавр">Барапазавр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D1%81%D0%B8%D0%BD%D0%B3%D0%B0" title="Барасинга">Барасинга</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B0%D1%88%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BB%D0%BE%D0%BF%D0%B0%D1%82%D0%BE%D0%BD%D0%BE%D0%B3" title="Барашковый лопатоног">Барашковый лопатоног</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D0%B4%D0%BE%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D0%B5%D0%BD%D0%BE%D1%82" title="Барбадосский енот">Барбадосский енот</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D1%80%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%B0%D1%82%D0%B0%D1%8F_%D0%BC%D1%8B%D1%88%D1%8C" title="Барбарийская полосатая мышь">Барбарийская полосатая мышь</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%83%D1%80%D1%83%D0%BB%D1%8B" title="Барбурулы">Барбурулы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%83%D1%81-%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BB%D0%B5%D0%BF%D0%B8%D1%81" title="Барбус-олиголепис">Барбус-олиголепис</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%83%D1%81-%D1%82%D0%B8%D0%BA%D1%82%D0%BE" title="Барбус-тикто">Барбус-тикто</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B1%D1%83%D1%81%D1%8B" title="Барбусы">Барбусы</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B8%D0%B1%D0%B0%D0%BB" title="Барибал">Барибал</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B8%D0%B4%D1%8B" title="Бариды">Бариды</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B8%D0%BB%D1%8F%D0%BC%D0%B1%D0%B4%D0%B0" title="Барилямбда">Барилямбда</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B8%D0%BE%D0%BD%D0%B8%D0%BA%D1%81" title="Барионикс">Барионикс</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D1%80%D0%B8%D0%B9" title="Баритерий">Баритерий</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%BC%D0%B0%D0%BB%D0%B5%D0%B9_%D0%B7%D1%83%D0%B1%D0%B0%D1%81%D1%82%D1%8B%D0%B9" title="Бармалей зубастый">Бармалей зубастый</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D0%BE%D0%B7%D0%B0%D0%B2%D1%80" title="Барозавр">Барозавр</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D1%80%D0%B0%D0%BA%D1%83%D0%B4%D1%8B" title="Барракуды">Барракуды</a></li>
            <li><a href="/wiki/%D0%91%D0%B0%D1%80%D1%81%D0%B1%D0%BE%D0%BB%D0%B4%D0%B8%D1%8F" title="Барсболдия">Барсболдия</a></li></ul></div></div></div>(<a href="/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp;filefrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;pageuntil=%D0%90%D1%84%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D1%82%D1%80%D0%BE%D0%B3%D0%BE%D0%BD%D1%8B&amp;subcatfrom=%3Cb%3E%D0%AF%3C%2Fb%3E#mw-pages" title="Категория:Животные по алфавиту">Предыдущая страница</a>) (<a href="/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&amp;filefrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;subcatfrom=%3Cb%3E%D0%AF%3C%2Fb%3E&amp;pagefrom=%D0%91%D0%B0%D1%80%D1%81%D1%83%D0%BA#mw-pages" title="Категория:Животные по алфавиту">Следующая страница</a>)
            </div>
            """, 'lxml')
        self.test_pages_container = self.bf.find('div', id="mw-pages")

    def test_count_letter_group(self):
        count_letter_group(self.letters, self.test_pages_container)
        self.assertEqual(self.letters, {'А': 86, 'Б': 114})

    def test_total_count(self):
        self.letters = {}
        parse_page(URL, self.letters)
        print(self.letters)
        total_count = sum(self.letters.values())
        self.assertEqual(total_count, 46286)

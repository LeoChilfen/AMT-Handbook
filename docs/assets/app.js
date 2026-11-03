(function(){
  var data = window.AMT_DATA || [];
  var cardsData = window.AMT_CARDS || [];
  var cardsByChapter = {};
  cardsData.forEach(function(s){ cardsByChapter[s.chapter] = s; });
  var bySlug = {};
  var order = [];
  data.forEach(function(g){ g.chapters.forEach(function(c){ c.group = g; bySlug[c.slug] = c; order.push(c); }); });

  var nav = document.getElementById('nav');
  var content = document.getElementById('content');
  var search = document.getElementById('search');
  var sidebar = document.getElementById('sidebar');
  var menuBtn = document.getElementById('menuBtn');

  function pad2(n){ var m = String(n).match(/^(\d+)([ab]?)$/); if (!m) return n; return (m[1].length < 2 ? '0' + m[1] : m[1]) + m[2]; }

  function buildNav(){
    var html = '';
    if (cardsData.length){
      html += '<div class="nav-group"><h3>学习卡片 · Study cards</h3>' +
        '<a class="nav-link" href="#/cards" data-slug="__cards__">' +
        '<span class="row"><span class="num">★</span><span class="ttl">全部学习卡片</span></span></a></div>';
    }
    data.forEach(function(g){
      html += '<div class="nav-group" data-group="' + g.slug + '"><h3>' + g.en + ' · ' + g.zh + '</h3>';
      g.chapters.forEach(function(c){
        html += '<a class="nav-link" href="#/' + c.slug + '" data-slug="' + c.slug + '">' +
          '<span class="row"><span class="num">' + pad2(c.num) + '</span>' +
          '<span class="ttl">' + esc(c.titleEn || ('Ch ' + c.num)) + '</span></span></a>';
      });
      html += '</div>';
    });
    nav.innerHTML = html;
  }

  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function markActive(slug){
    [].forEach.call(nav.querySelectorAll('.nav-link'), function(a){
      a.classList.toggle('active', a.getAttribute('data-slug') === slug);
    });
  }

  function setTitle(t){ document.title = t ? (t + ' · AMT Handbook 中文笔记') : 'AMT Handbook · 中文笔记'; }

  function renderHome(){
    var total = order.length;
    var html = '<div class="hero"><h1>AMT Handbook 中文笔记</h1>' +
      '<p class="lead">FAA《Aviation Maintenance Technician Handbook》三册全书的中文精读笔记，共 ' + total +
      ' 份，每章 8 个小节。第 7 节已改为 <strong>TECC 式英语完形填空</strong>：题干与选项取自本章英文术语，答案后附中文语法 / 词义解析。</p>' +
      '<div class="cards">';
    data.forEach(function(g){
      html += '<a class="card" href="#/index"><span class="k">' + g.en + '</span>' +
        '<div class="t">' + g.zh + ' · ' + g.count + ' 份</div>' +
        '<div class="d">点开总索引，逐章阅读</div></a>';
    });
    html += '</div></div>' +
      '<h2>怎么用</h2>' +
      '<ul>' +
      '<li>左侧目录按三册分组，点章节即可打开；顶部搜索框按章节标题过滤（快捷键 <code>/</code>）。</li>' +
      '<li>每章固定 8 节：一句话 → 要点 → 术语对照 → 关键数字 → 结构部件 → 检查维修 → <b>高频考点（完形填空）</b> → 易混点。</li>' +
      '<li>完形填空先自己做，答案与解析在每条题目的「答案与解析」小节里。</li>' +
      '</ul>' +
      '<p style="color:#8a8f98;font-size:14px">原始 Markdown 文件在仓库 <code>notes/</code> 目录，可直接用 Obsidian 或 VS Code 打开。</p>';
    content.innerHTML = html;
    markActive(null);
    setTitle('');
  }

  function renderIndex(){
    var html = '<div class="crumb">总索引</div><h1>44 章总索引</h1>' +
      '<p style="color:#4b5563;font-size:14.5px;margin-top:-8px">每章一句话概括，点标题进入全文。</p>';
    data.forEach(function(g){
      html += '<section class="idx-book"><h2>' + g.en + ' · ' + g.zh + '（' + g.count + ' 份）</h2>';
      g.chapters.forEach(function(c){
        html += '<div class="idx-item"><a href="#/' + c.slug + '">' +
          '<span class="idx-num">Ch ' + c.num + '</span>' + esc(c.titleEn || ("Ch " + c.num)) + '</a>' +
          '<span>' + esc(c.summary || c.titleZh || "") + '</span></div>';
      });
      html += '</section>';
    });
    content.innerHTML = html;
    markActive(null);
    setTitle('总索引');
  }

  function renderChapter(slug, anchor){
    var c = bySlug[slug];
    if (!c){ content.innerHTML = '<div class="loading">没有找到这一章。<a href="#/">回到首页</a></div>'; return; }
    var idx = order.indexOf(c);
    var prev = idx > 0 ? order[idx - 1] : null;
    var next = idx < order.length - 1 ? order[idx + 1] : null;

    fetch('pages/' + slug + '.html').then(function(r){
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.text();
    }).then(function(html){
      var toc = '';
      if (c.headings && c.headings.length){
        toc = '<div class="toc"><b>本页目录</b>' + c.headings.map(function(h){
          return '<a href="#/' + slug + '/' + h.id + '">' + esc(h.text) + '</a>';
        }).join('') + '</div>';
      }
      var pager = '<div class="pager">' +
        '<div class="grow">' + (prev ? '<a href="#/' + prev.slug + '">← Ch ' + prev.num + ' ' + esc(prev.titleEn) + '</a>' : '') + '</div>' +
        '<div class="grow" style="text-align:right">' + (next ? '<a href="#/' + next.slug + '">Ch ' + next.num + ' ' + esc(next.titleEn) + ' →</a>' : '') + '</div>' +
        '</div>';
      var crumb = '<div class="crumb">' + c.bookEn + ' · ' + c.bookZh + ' / Ch ' + c.num + '</div>';
      var h1end = html.indexOf('</h1>');
      if (toc && h1end > -1){ html = html.slice(0, h1end + 5) + toc + html.slice(h1end + 5); }
      content.innerHTML = crumb + html + pager;
      markActive(slug);
      setTitle('Ch ' + c.num + ' ' + (c.titleEn || ''));
      if (anchor){
        var el = document.getElementById(anchor);
        if (el){ el.scrollIntoView({block: 'start'}); } else { window.scrollTo(0, 0); }
      } else {
        window.scrollTo(0, 0);
      }
    }).catch(function(err){
      content.innerHTML = '<div class="loading">这一页加载失败（' + err.message + '）。请刷新重试。</div>';
    });
  }

  function renderCardsIndex(){
    var total = 0;
    cardsData.forEach(function(s){ total += s.count; });
    var html = '<div class="hero"><h1>学习卡片</h1>' +
      '<p class="lead">按每章<b>二级目录</b>拆分的学习卡片：每张覆盖一个大节（含其下的小标题），包含 <b>手册原文</b>、<b>专业翻译</b>、<b>专业词汇解析</b> 与 <b>语法解析</b>。' +
      (total ? '当前共 ' + total + ' 张，覆盖 ' + cardsData.length + ' 章。' : '') + '</p></div>';
    var curBook = '';
    cardsData.forEach(function(s){
      if (s.book !== curBook){
        curBook = s.book;
        html += '<h2 class="idx-book">' + esc(s.bookEn) + ' · ' + esc(s.bookZh) + '</h2>';
      }
      html += '<div class="idx-item">' +
        '<a class="idx-num" href="#/cards/' + s.chapter + '">Ch ' + pad2(s.num) + '</a>' +
        '<div class="idx-main"><a class="idx-title" href="#/cards/' + s.chapter + '">' + esc(s.titleEn) + '</a>' +
        '<div class="idx-sum">' + s.count + ' 张卡片</div></div></div>';
    });
    content.innerHTML = html;
    markActive('__cards__');
    setTitle('学习卡片');
    window.scrollTo(0, 0);
  }

  function renderCardSet(chapterSlug){
    var s = cardsByChapter[chapterSlug];
    if (!s){ content.innerHTML = '<div class="loading">没有找到这组卡片。<a href="#/cards">返回卡片目录</a></div>'; return; }
    var html = '<div class="crumb"><a href="#/cards">学习卡片</a> / ' + esc(s.bookEn) + ' · ' + esc(s.bookZh) + '</div>' +
      '<h1>Ch ' + pad2(s.num) + ' · ' + esc(s.titleEn) + '</h1>' +
      '<p class="lead">共 ' + s.count + ' 张卡片，按节顺序排列。</p><ol class="card-list">' +
      s.cards.map(function(c){
        return '<li><a href="#/card/' + c.slug + '">' + esc(c.title) + '</a></li>';
      }).join('') + '</ol>';
    content.innerHTML = html;
    markActive(chapterSlug);
    setTitle('学习卡片 · Ch ' + s.num);
    window.scrollTo(0, 0);
  }

  function renderCard(slug){
    var set = null, idx = -1;
    cardsData.forEach(function(s){
      s.cards.forEach(function(c, i){ if (c.slug === slug){ set = s; idx = i; } });
    });
    if (!set){ content.innerHTML = '<div class="loading">没有找到这张卡片。<a href="#/cards">返回卡片目录</a></div>'; return; }
    var prev = idx > 0 ? set.cards[idx - 1] : null;
    var next = idx < set.cards.length - 1 ? set.cards[idx + 1] : null;
    fetch('cards/' + slug + '.html').then(function(r){
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.text();
    }).then(function(html){
      var crumb = '<div class="crumb"><a href="#/cards">学习卡片</a> / <a href="#/cards/' + set.chapter + '">' +
        esc(set.bookEn) + ' Ch ' + pad2(set.num) + '</a> / 第 ' + (idx + 1) + ' 节</div>';
      var pager = '<div class="pager">' +
        '<div class="grow">' + (prev ? '<a href="#/card/' + prev.slug + '">← ' + esc(prev.title) + '</a>' : '') + '</div>' +
        '<div class="grow" style="text-align:right">' + (next ? '<a href="#/card/' + next.slug + '">' + esc(next.title) + ' →</a>' : '') + '</div>' +
        '</div>';
      content.innerHTML = crumb + html + pager;
      markActive(set.chapter);
      setTitle((set.cards[idx] ? set.cards[idx].title : '') + ' · 学习卡片');
      window.scrollTo(0, 0);
    }).catch(function(err){
      content.innerHTML = '<div class="loading">卡片加载失败（' + err.message + '）。</div>';
    });
  }

  function route(){
    var h = location.hash.replace(/^#\/?/, '');
    var parts = h.split('/');
    var slug = parts[0];
    if (!slug){ renderHome(); }
    else if (slug === 'index'){ renderIndex(); }
    else if (slug === 'cards'){
      if (parts[1]){ renderCardSet(parts[1]); } else { renderCardsIndex(); }
    }
    else if (slug === 'card' && parts[1]){ renderCard(parts[1]); }
    else {
      var anchor = parts[1] ? decodeURIComponent(parts[1]) : '';
      renderChapter(slug, anchor);
    }
    sidebar.classList.remove('open');
  }

  search.addEventListener('input', function(){
    var q = search.value.trim().toLowerCase();
    [].forEach.call(nav.querySelectorAll('.nav-link'), function(a){
      var c = bySlug[a.getAttribute('data-slug')];
      var hay = (c.titleEn + ' ' + c.titleZh + ' ' + c.num + ' ' + c.bookZh + ' ' + c.bookEn).toLowerCase();
      a.style.display = (!q || hay.indexOf(q) > -1) ? '' : 'none';
    });
    [].forEach.call(nav.querySelectorAll('.nav-group'), function(g){
      var vis = [].some.call(g.querySelectorAll('.nav-link'), function(a){ return a.style.display !== 'none'; });
      g.style.display = vis ? '' : 'none';
    });
  });

  document.addEventListener('keydown', function(e){
    if (e.key === '/' && document.activeElement !== search){ e.preventDefault(); search.focus(); }
    if (e.key === 'Escape' && document.activeElement === search){ search.value = ''; search.dispatchEvent(new Event('input')); search.blur(); }
  });

  menuBtn.addEventListener('click', function(){ sidebar.classList.toggle('open'); });
  window.addEventListener('hashchange', route);

  buildNav();
  route();
})();

(function(){
  var data = window.AMT_DATA || [];
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
    data.forEach(function(g){
      html += '<div class="nav-group" data-group="' + g.slug + '"><h3>' + g.en + ' · ' + g.zh + '</h3>';
      g.chapters.forEach(function(c){
        html += '<a class="nav-link" href="#/' + c.slug + '" data-slug="' + c.slug + '">' +
          '<span class="row"><span class="num">' + pad2(c.num) + '</span>' +
          '<span class="ttl">' + esc(c.titleEn || ('Ch ' + c.num)) + '</span></span>' +
          (c.titleZh ? '<span class="zh">' + esc(c.titleZh) + '</span>' : '') + '</a>';
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
        html += '<div class="idx-item"><a href="#/' + c.slug + '">Ch ' + c.num + '</a>' +
          '<span>' + esc(c.summary || c.titleZh || c.titleEn) + '</span></div>';
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

  function route(){
    var h = location.hash.replace(/^#\/?/, '');
    var parts = h.split('/');
    var slug = parts[0];
    if (!slug){ renderHome(); }
    else if (slug === 'index'){ renderIndex(); }
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

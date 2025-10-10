(function(){
  try{
    var base = (window.SPHINX_HTML_BASEURL || "").toString();
    var path = location.pathname.replace(/index\.html$/, '');
    var url = (base || location.origin) + path;
    var link = document.querySelector('link[rel="canonical"]');
    if(!link){ link = document.createElement('link'); link.rel='canonical'; document.head.appendChild(link); }
    link.href = url;
  }catch(e){}
})();
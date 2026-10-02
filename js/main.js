(function(){
document.documentElement.classList.add('js-motion');
var b=document.querySelector('.burger'),u=document.querySelector('nav ul');
if(b)b.addEventListener('click',function(){var o=u.classList.toggle('open');b.setAttribute('aria-expanded',o)});
var el=document.getElementById('typed');
if(el){var w=JSON.parse(el.dataset.words),i=0;
 var still=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 el.textContent=w[0];
 if(!still)setInterval(function(){
document.documentElement.classList.add('js-motion');i=(i+1)%w.length;el.textContent=w[i]},2400);}
var reveals=document.querySelectorAll('.reveal');
if('IntersectionObserver' in window){var observer=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target)}})},{threshold:.12});reveals.forEach(function(el){observer.observe(el)});}else{reveals.forEach(function(el){el.classList.add('is-visible')});}
document.querySelectorAll('.filters').forEach(function(f){
 f.addEventListener('click',function(e){var t=e.target.closest('button');if(!t)return;
  f.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
  var c=t.dataset.f;document.querySelectorAll('[data-cat]').forEach(function(n){n.classList.toggle('hide',c!=='all'&&n.dataset.cat.split(' ').indexOf(c)<0)})})});
})();


const workflowData = {
  rag: {desc:'A retrieval-augmented generation flow that grounds responses in source documents.',nodes:[['01','Ingest','PDFs, text, data'],['02','Chunk & embed','Semantic vectors'],['03','Retrieve','Vector search'],['04','Generate','Grounded answer']]},
  agent: {desc:'A tool-using agent loop that plans work, invokes tools, observes results and responds.',nodes:[['01','Plan','Break down task'],['02','Use tools','MCP / APIs'],['03','Observe','Inspect results'],['04','Respond','Memory-aware output']]},
  vision: {desc:'A computer-vision workflow from image/video input to detection and interpretable output.',nodes:[['01','Capture','Image / video'],['02','Preprocess','Frames & resize'],['03','Infer','YOLO / PyTorch'],['04','Present','Alerts & insights']]}
};
document.querySelectorAll('.workflow-tab').forEach(button => {
  button.addEventListener('click', () => {
    const flow = workflowData[button.dataset.flow];
    if (!flow) return;
    document.querySelectorAll('.workflow-tab').forEach(tab => {
      const active = tab === button;
      tab.classList.toggle('active', active);
      tab.setAttribute('aria-selected', String(active));
    });
    const track = document.getElementById('workflow-track');
    if (track) {
      track.innerHTML = flow.nodes.map((node,i) =>
        `<div class="workflow-node"><span>${node[0]}</span><b>${node[1]}</b><small>${node[2]}</small></div>${i<flow.nodes.length-1?'<i aria-hidden="true">→</i>':''}`
      ).join('');
    }
    const description = document.getElementById('workflow-description');
    if (description) description.textContent = flow.desc;
  });
});

// Bradford native editable frame; all illustration positions stay empty.
export const canvas={width:1681,height:936};
export const fonts={heading:'Comic Sans MS',body:'Comic Sans MS',math:'Times New Roman'};
const C={ink:'#101329',purple:'#352153',blue:'#1559A4',amber:'#DCA12A',green:'#007345'};
const grad=(a,b)=>({type:'gradient',gradientKind:'linear',angleDeg:90,stops:[{offset:0,color:a},{offset:100000,color:b}]});
export function author(pres,project){
 const native=[],counts=[];
 for(const guide of [false,true]){
  const s=pres.slides.add({width:canvas.width,height:canvas.height,background:{fill:'#FFFFFF'}});
  const record=v=>{if(!guide)native.push(v);};
  const shape=(name,geometry,b,fill='none',stroke='none',width=0,radius)=>{
   const o=s.shapes.add({name,geometry,position:{left:b[0],top:b[1],width:b[2],height:b[3]},fill,line:{style:'solid',fill:stroke,width},...(radius?{borderRadius:radius}:{})});
   record({id:name,kind:'shape',bbox:b});return o;
  };
  const box=(name,b,fill,stroke,r=24)=>shape(name,'roundRect',b,fill,stroke,3.8,r);
  const tx=(id,label,b,size=28,color=C.ink,align='center',font=fonts.body,bold=true,italic=false)=>{
   const t=shape('TXT_'+id,'textbox',b);t.text=label;t.text.style={fontSize:size,typeface:font,bold,italic,color,alignment:align,verticalAlignment:'middle',insets:0,wrap:'square',autoFit:'none',lineSpacing:1.02};
   if(!guide)native[native.length-1]={id:'TXT_'+id,kind:'text',label,bbox:b,font,size};return t;
  };
  const path=(id,points,color=C.blue,width=6,arrow=true)=>{
   const xs=points.map(p=>p[0]),ys=points.map(p=>p[1]),left=Math.min(...xs),top=Math.min(...ys),w=Math.max(1,Math.max(...xs)-left),h=Math.max(1,Math.max(...ys)-top);
   const commands=points.map((p,i)=>i?{lineTo:{x:p[0]-left,y:p[1]-top}}:{moveTo:{x:p[0]-left,y:p[1]-top}});
   s.shapes.add({name:'LINE_'+id,geometry:'custom',position:{left,top,width:w,height:h},fill:'none',line:{style:'solid',fill:color,width},customPaths:[{width:w,height:h,commands}]});
   record({id:'LINE_'+id,kind:'connector',points,color});
   if(arrow){
    const a=points.at(-2),b=points.at(-1),len=Math.hypot(b[0]-a[0],b[1]-a[1]),ux=(b[0]-a[0])/len,uy=(b[1]-a[1])/len;
    const pp=[b,[b[0]-ux*16-uy*10,b[1]-uy*16+ux*10],[b[0]-ux*16+uy*10,b[1]-uy*16-ux*10]];
    const x=Math.min(...pp.map(p=>p[0])),y=Math.min(...pp.map(p=>p[1])),ww=Math.max(1,Math.max(...pp.map(p=>p[0]))-x),hh=Math.max(1,Math.max(...pp.map(p=>p[1]))-y);
    s.shapes.add({name:'HEAD_'+id,geometry:'custom',position:{left:x,top:y,width:ww,height:hh},fill:color,line:{fill:color,width:.5},customPaths:[{width:ww,height:hh,commands:[{moveTo:{x:pp[0][0]-x,y:pp[0][1]-y}},{lineTo:{x:pp[1][0]-x,y:pp[1][1]-y}},{lineTo:{x:pp[2][0]-x,y:pp[2][1]-y}},{close:{}}]}]});record({id:'HEAD_'+id,kind:'arrowhead'});
   }
  };
  box('TITLE',[28,10,855,88],grad('#552076','#2B143E'),'#28123C',24);
  box('MECHANISM',[20,120,330,794],grad('#F6F0FC','#F1E8F9'),C.purple);
  box('STANDARDS',[378,125,318,230],grad('#FFF1C6','#FFF9E7'),'#D6B25A');
  box('UNKNOWN',[378,393,318,225],grad('#EDF8E3','#F7FBEE'),'#99BE76');
  box('BLANK',[378,654,318,229],grad('#E2F6FF','#F2FCFF'),'#71CDE9');
  box('MEASUREMENT',[1189,127,443,407],grad('#EADFFB','#F6F0FC'),C.purple);
  box('CORRECTION',[1199,589,435,129],grad('#DCEBFA','#F3F9FF'),'#1865BB',20);
  box('CALIBRATION',[1175,791,241,108],grad('#FFF0C5','#FFF8E2'),'#E3A433',20);
  box('ESTIMATE',[1435,791,233,108],grad('#DAF0D1','#F0FAEC'),'#006C44',20);
  path('protein_binding',[[182,568],[182,626]],C.blue,8);
  path('standards_to_bound',[[699,242],[793,242]]);
  path('unknown_to_bound',[[699,512],[795,512]]);
  path('blank_to_reagent',[[699,795],[795,795]]);
  path('standard_measurement',[[912,242],[1134,242],[1134,310],[1180,310]]);
  path('unknown_measurement',[[912,512],[1134,512],[1134,310]],C.blue,6,false);
  path('blank_measurement',[[912,795],[1162,795],[1162,488],[1180,488]]);
  path('measurement_to_correction',[[1408,535],[1408,580]]);
  path('corrected_standards',[[1282,720],[1282,782]],C.amber);
  path('corrected_unknown',[[1559,720],[1559,782]],C.green);
  path('calibration_to_estimate',[[1417,845],[1428,845]],C.amber,7);
  for(const o of project.occurrences){
   const ph=shape('ASSET_'+o.asset_id+'_'+o.id,'rect',(o.fit_bbox??o.bbox),'none','none',0);
   if(guide){
    ph.fill='#DAE9F6/32';ph.line={style:'dashed',fill:'#7D94A9',width:1.2};
    const [x,y,w,h]=o.fit_bbox??o.bbox;
    shape('GUIDE_BADGE_'+o.id,'roundRect',[x+w-47,y+h-23,45,22],'#FFFFFF/95','#8298AB',.7,4);
    tx('GUIDE_'+o.id,o.asset_id,[x+w-46,y+h-23,43,22],16,'#33516B','center',fonts.math,true);
   }
  }
  tx('title','Bradford protein assay',[42,17,825,74],55,'#FFFFFF');
  tx('mechanism_heading','Protein-dye binding',[37,133,294,44],30);
  tx('protein_label','Protein\n(unknown or standard)',[46,325,280,56],25);
  tx('plus','+',[157,382,55,54],52);
  tx('dye_label','Coomassie G-250',[53,435,264,38],24);
  tx('bound_label','Blue protein-dye\ncomplex\n(stabilized blue form)',[42,807,286,82],25);
  tx('standards_heading','Known standards',[390,138,294,44],32);
  tx('unknown_heading','Unknown sample',[390,405,294,46],32);
  tx('blank_heading','Reagent blank',[390,667,294,46],32);
  tx('dye_standards','Coomassie\nG-250',[745,123,120,49],20);
  tx('dye_unknown','Coomassie\nG-250',[745,393,120,49],20);
  tx('dye_blank','Coomassie\nG-250',[745,673,120,49],20);
  tx('binding_standards','Protein-dye binding\n(standards)',[750,303,250,51],24);
  tx('binding_unknown','Protein-dye binding\n(unknown)',[750,578,250,51],24);
  tx('measurement_heading','Read absorbance\nat 595 nm',[1210,141,399,80],35);
  tx('correction_heading','Blank correction',[1218,598,397,44],33);
  tx('calibration','Calibration\nfrom standards',[1187,805,218,75],27);
  tx('estimate','Estimate\nprotein amount',[1443,805,217,75],27);
  // Editable math with smaller lowered labels, not raster equation images.
  tx('A_corrected_base','A',[1224,649,23,42],32,C.ink,'left',fonts.math,false,true);
  tx('A_corrected_sub','corrected',[1247,672,85,26],21,C.ink,'left',fonts.math,false);
  tx('equals','=',[1336,649,25,42],32,C.ink,'left',fonts.math,false);
  tx('A_sample_base','A',[1368,649,23,42],32,C.ink,'left',fonts.math,false,true);
  tx('A_sample_sub','sample',[1391,672,62,26],21,C.ink,'left',fonts.math,false);
  tx('minus','−',[1456,649,25,42],32,C.ink,'left',fonts.math,false);
  tx('A_blank_base','A',[1488,649,23,42],32,C.ink,'left',fonts.math,false,true);
  tx('A_blank_sub','blank',[1511,672,62,26],21,C.ink,'left',fonts.math,false);
  tx('screen_A','A',[1450,323,22,34],26,C.ink,'left',fonts.math,false,true);
  tx('screen_595','595',[1472,337,32,20],16,C.ink,'left',fonts.math,false);
  tx('screen_nm','nm',[1508,331,29,25],19,C.ink,'left',fonts.math,false);
  s.speakerNotes.text='Approved concept: Bradford-B-r1. Source: Marion M. Bradford, Analytical Biochemistry 72 (1976) 248–254, DOI 10.1016/0003-2697(76)90527-3; paper: https://hoffman.cm.utexas.edu/courses/bradford_assay.pdf. Standards, unknown and blank are measured separately with the same instrument; joining measurement lines do not mix physical samples. Protein/dye artwork is conceptual. All text, panels, equation components and arrows are native editable shapes. Every illustration position remains empty for manual assembly. The nonfunctional purple instrument arrow is omitted. Slide 2 is the numbered placement guide.';
  counts.push({guide,slideId:s.id,nativeObjects:s.shapes.items.length});
 }
 return {canvas,fonts,nativeElements:native,counts};
}


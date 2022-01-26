# [web网页端上传用户头像，后端获取后，返回路径给前端做展示](https://www.cnblogs.com/dongmodify/p/13765168.html)

上传头像的实现思路，以前就有的，不过二次修改移动框架的时候，被自己给坑了。所以记一下吧，方便路过的朋友。

```
  分析用户操作，一般都是前端选中图片后，做本地预览。然后submit提交给后端服务器。

  这边记录下，自己的思路。
  第一步：选择图片

  第二步，通过选择事件，选择图片，然后提交服务器。等待服务器返回图片上传好的路径后。做本地展示。（更高级的操作是，先加载本地预览，上传成功后替换本地预览）。

  第三步，点击提交按钮。上传当前服务器返回的文件名，存入数据库。然后重新加载本页面。新用户头像上传完毕。

  这方法有缺陷，但是简单直接，大家可能会想到服务器上图片多出来了。不过这个是在登陆成功以后操作。在上传前可以判断先用户是否登陆。若想删除没用到的图片。那就要辛苦下，后端做个查询。然后操作文件删除。
  可能有人会说，给前端留个删除图片。

  //上传头像-后端接收方法(thinkphp-框架)
public function upload(){
    // 获取上传文件表单字段名，不传文件会报错。
    $fileKey = array_keys(request()->file());//获取文件名。
    $file = request()->file($fileKey['0']);//如果想传多图。偷懒，循环下这个方法。多拿几个
    $info = $file->validate(['ext' => 'jpg,png,gif,jpeg'])->move('uploads');//判断图片类型。
    $result['code'] = 1;
    $result['title'] = '头像!';
    $path=str_replace('\\','/',$info->getSaveName());//移动后拿到的文件名称
    $result['url'] = '/uploads/'. $path;//拼接返回目录，跟前端做显示准备
    return json(['code'=>0, 'msg'=>'上传成功', 'data'=>$result]);//json返回数据。如果要考虑错误情况，可以在加个判断。
}

  //前端静态页面代码 .注意点
        {1.id=form4
         2. class="upload-btn"
         3.input框中的 onchange方法（upload_cover上传方法）。id='picture_upload' 
         4.隐藏的newhead方法。默认值为空，因为没有值要传。    
         5.MyButton1=提交图片上传以后的newhead值，给后端的。          
        }
          <form id="form4">
                                <div class="upload-btn">
                                    <button class="btn btn-submit" >选择要上传的图片 <input   onchange="upload_cover(this)"  id="picture_upload" name="file"  type="file" class="upload-input"></button>
                                </div>
                                <div class="btn btn-tj">
                                    <input type="hidden" value="" name="newhead" id="newhead" />
                                    <input type="submit" value="确定提交" id="MyButton1" class="btn btn-submit">
                                </div>
                            </form>


              //上传图片  　
            function upload_cover(obj) {//obj就是input文件框的所有内容
                      ajax_upload(obj.id, function(data) {//匿名函数，执行上传成功以后的操作。核心在ajax_upload方法中。
                          console.log('test');//obj.id=picture_upload 给上传js
                    var isrc = data.data.url.replace(/\/\//g, '/');//
                    console.log(isrc);
                    $('.avatarimg').attr('src',isrc); //给<input>的src赋值去显示图片
                    // //更换页面显示4个图
                    $('.rightimg').attr('src',isrc); //给<input>的src赋值去显示图片
                    $('#newhead').attr('value',isrc);//显示成功后，就该提交form表单了。
                });
            }

               function ajax_upload(feid, callback) {//feid上传图片插件要通过这个id,也就是picture_upload 来拿文件资源。callback为这个函数的回调值，会返给upload_cover方法，做页面显示时使用。
                    $.ajaxFileUpload({
                        fileElementId: feid,
                        url:"/index.php/home/webmember/upload",//上传文件的路径
                        type: 'post',//传输方式。大小在7mb,左右，不要超限制，或者看下后端最大图片限制。
                        dataType: 'json',//数据类型
                        secureuri: false,//是否安全模式
                        async : true,//是否是异步
                        success: function(data) {
                            if (callback) callback.call(this, data);//如果有回调，返回给调用的方法。
                        },
                              error: function(data, status, e) {  //提交失败自动执行的处理函数。
                            console.error(e);//控制台输出，方便前端调试。
                        }
                    });
              }
              //前端验证图片格式是否在要求的格式内，这里没有用，因为后端已经验证了。      
        function image_check(feid) { //自己添加的文件后缀名的验证
                var img = document.getElementById(feid);
                    return /.(jpg|png|gif|bmp)$/.test(img.value)?true:(function() {
                    layer.msg('图片格式仅支持jpg、png、gif、bmp格式，且区分大小写.');
                    return false;
                })();
            }
        
  //
        //更换头像确认操作
   $(document).on('click', '#MyButton1', function () {
          //检查字段.后端验证。这里能提交一个，那一个页面就能提交多个，希望对大家有帮助。
          $.ajax({
              type: "POST",
              dataType: "json",
              url: "/index.php/home/webmember/upavatar" ,//修改头像接口
              data: $('#form4').serialize(),//这里写下为什么用这个，前端对这个id下面的form4做了序列化操作。发送到后端，所有的当前form中，input,只要带name属性的，都能接收到。前端知识，还没被废弃，个人觉得挺好用的。后端接收也很轻松。
              success: function (res){
                  layer.msg(res.msg)
                  setInterval(function () {
                      window.location.reload()
                  }, 2000)
              },
              error : function() {
                  alert("异常提交");
              }
          });
            })
```
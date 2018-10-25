### 过滤器


| 过滤器          | 描述                | 示例                                                                                   |  
| --------------- | ------------------- | -------------------------------------------------------------------------------------- | 
| upper	          | 以大写方式输出	| {{ user.name \| upper }}                                                                |
| add	          | 给value加上一个数值	| {{ user.age \| add:”5” }}                                                             |
| addslashes	  | 单引号加上转义号	|                                                                                        |
| capfirst	  | 第一个字母大写	| {{ ‘good’| capfirst }} 返回”Good”                                                  |
| center	  | 输出指定长度的字符串，把变量居中	| {{ “abcd”| center:”50” }}                                          |
| cut	          | 删除指定字符串	| {{ “You are not a Englishman” | cut:”not” }}                                       |
| date	          | 格式化日期|	                                                                                                 |
| default	  | 如果值不存在，则使用默认值代替| {{ value | default:”(N/A)” }}                                              |
| default_if_none | 如果值为None, 则使用默认值代替|     	                                                                 |
| dictsort	  | 按某字段排序，变量必须是一个dictionary	| {% for moment in moments | dictsort:”id” %}                  |  
| dictsortreversed| 按某字段倒序排序，变量必须是dictionary	 |                                                               |
| divisibleby	  | 判断是否可以被数字整除 | {{ 224 | divisibleby:2 }}  返回 True                                                |
| escape	  | 按HTML转义，比如将”<”转换为”&lt”|	                                                                 |
| filesizeformat  | 增加数字的可读性，转换结果为13KB,89MB,3Bytes等	| {{ 1024 | filesizeformat }} 返回 1.0KB                 |
| first	          | 返回列表的第1个元素，变量必须是一个列表	 |                                                               |
| floatformat	  | 转换为指定精度的小数，默认保留1位小数	| {{ 3.1415926 | floatformat:3 }} 返回 3.142  四舍五入           |
| get_digit	  | 从个位数开始截取指定位置的数字|	{{ 123456 | get_digit:’1’}}                                            |
| join	          | 用指定分隔符连接列表	| {{ [‘abc’,’45’] | join:’*’ }} 返回 abc*45                                |
| length          | 返回列表中元素的个数或字符串长度|	                                                                         |
| length_is	  | 检查列表，字符串长度是否符合指定的值|	{{ ‘hello’| length_is:’3’ }}                                 |
| linebreaks	  | 用'<p>'或'<br>'标签包裹变量	| {{ “Hi\n\nDavid”|linebreaks }} 返回<p>Hi</p><p>David</p>                     |
| linebreaksbr	  | 用<br/>标签代替换行符	|                                                                                |
| linenumbers	  | 为变量中的每一行加上行号	 |                                                                               |   
| ljust	          | 输出指定长度的字符串，变量左对齐|	{{‘ab’|ljust:5}}返回 ‘ab   ’                                         |
| lower	          | 字符串变小写	 |                                                                                       |
| make_list	  | 将字符串转换为列表	 |                                                                                       |  
| pluralize	  | 根据数字确定是否输出英文复数符号|	                                                                         |
| random	  | 返回列表的随机一项	 |                                                                                       | 
| removetags	  | 删除字符串中指定的HTML标记|	{{value | removetags: “h1 h2”}}                                                |  
| rjust	          | 输出指定长度的字符串，变量右对齐|	                                                                         | 
| slice           | 切片操作， 返回列表	|{{[3,9,1] | slice:’:2’}} 返回 [3,9]{{ 'asdikfjhihgie' | slice:':5' }} 返回 ‘asdik’  |
| slugify	  | 在字符串中留下减号和下划线，其它符号删除，空格用减号替换|	{{ '5-2=3and5 2=3' | slugify }} 返回 5-23and5-23 |
| stringformat	  | 字符串格式化，语法同python	 |                                                                               | 
| time	          | 返回日期的时间部分	 |                                                                                       |
| timesince	  | 以“到现在为止过了多长时间”显示时间变量|	结果可能为 45days, 3 hours                                       |
| timeuntil	  | 以“从现在开始到时间变量”还有多长时间显示时间变量|	                                                         |
| title	          | 每个单词首字母大写	 |                                                                                       |
| truncatewords	  | 将字符串转换为省略表达方式|	{{ 'This is a pen' | truncatewords:2 }}返回                                      |
| This is ...     |                                                                                                              |
| truncatewords_html|同上，但保留其中的HTML标签|	 {{ '<p>This is a pen</p>' | truncatewords:2 }}返回<p>This is ...</p>    |
| urlencode	  | 将字符串中的特殊字符转换为url兼容表达方式|	{{ ‘http://www.aaa.com/foo?a=b&b=c’ | urlencode}}              |
| urlize          | 将变量字符串中的url由纯文本变为链接	 |                                                                       |
| wordcount	  | 返回变量字符串中的单词数	 |                                                                               |
| yesno	          | 将布尔变量转换为字符串yes, no 或maybe|   {{ True | yesno }}<br>                                             |
                                                             {{ False | yesno }}<br>                                            
                                                             {{ None | yesno }}<br>                                             
                                                             返回<br>                                                            
                                                             yes<br>                                                             
                                                             no<br>                                                              
                                                             maybe<br>                                                          

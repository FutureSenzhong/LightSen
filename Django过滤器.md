### ������


| ������          | ����                | ʾ��                                                                                   |  
| --------------- | ------------------- | -------------------------------------------------------------------------------------- | 
| upper	          | �Դ�д��ʽ���	| {{ user.name \| upper }}                                                                |
| add	          | ��value����һ����ֵ	| {{ user.age \| add:��5�� }}                                                             |
| addslashes	  | �����ż���ת���	|                                                                                        |
| capfirst	  | ��һ����ĸ��д	| {{ ��good��| capfirst }} ���ء�Good��                                                  |
| center	  | ���ָ�����ȵ��ַ������ѱ�������	| {{ ��abcd��| center:��50�� }}                                          |
| cut	          | ɾ��ָ���ַ���	| {{ ��You are not a Englishman�� | cut:��not�� }}                                       |
| date	          | ��ʽ������|	                                                                                                 |
| default	  | ���ֵ�����ڣ���ʹ��Ĭ��ֵ����| {{ value | default:��(N/A)�� }}                                              |
| default_if_none | ���ֵΪNone, ��ʹ��Ĭ��ֵ����|     	                                                                 |
| dictsort	  | ��ĳ�ֶ����򣬱���������һ��dictionary	| {% for moment in moments | dictsort:��id�� %}                  |  
| dictsortreversed| ��ĳ�ֶε������򣬱���������dictionary	 |                                                               |
| divisibleby	  | �ж��Ƿ���Ա��������� | {{ 224 | divisibleby:2 }}  ���� True                                                |
| escape	  | ��HTMLת�壬���罫��<��ת��Ϊ��&lt��|	                                                                 |
| filesizeformat  | �������ֵĿɶ��ԣ�ת�����Ϊ13KB,89MB,3Bytes��	| {{ 1024 | filesizeformat }} ���� 1.0KB                 |
| first	          | �����б�ĵ�1��Ԫ�أ�����������һ���б�	 |                                                               |
| floatformat	  | ת��Ϊָ�����ȵ�С����Ĭ�ϱ���1λС��	| {{ 3.1415926 | floatformat:3 }} ���� 3.142  ��������           |
| get_digit	  | �Ӹ�λ����ʼ��ȡָ��λ�õ�����|	{{ 123456 | get_digit:��1��}}                                            |
| join	          | ��ָ���ָ��������б�	| {{ [��abc��,��45��] | join:��*�� }} ���� abc*45                                |
| length          | �����б���Ԫ�صĸ������ַ�������|	                                                                         |
| length_is	  | ����б��ַ��������Ƿ����ָ����ֵ|	{{ ��hello��| length_is:��3�� }}                                 |
| linebreaks	  | ��'<p>'��'<br>'��ǩ��������	| {{ ��Hi\n\nDavid��|linebreaks }} ����<p>Hi</p><p>David</p>                     |
| linebreaksbr	  | ��<br/>��ǩ���滻�з�	|                                                                                |
| linenumbers	  | Ϊ�����е�ÿһ�м����к�	 |                                                                               |   
| ljust	          | ���ָ�����ȵ��ַ��������������|	{{��ab��|ljust:5}}���� ��ab   ��                                         |
| lower	          | �ַ�����Сд	 |                                                                                       |
| make_list	  | ���ַ���ת��Ϊ�б�	 |                                                                                       |  
| pluralize	  | ��������ȷ���Ƿ����Ӣ�ĸ�������|	                                                                         |
| random	  | �����б�����һ��	 |                                                                                       | 
| removetags	  | ɾ���ַ�����ָ����HTML���|	{{value | removetags: ��h1 h2��}}                                                |  
| rjust	          | ���ָ�����ȵ��ַ����������Ҷ���|	                                                                         | 
| slice           | ��Ƭ������ �����б�	|{{[3,9,1] | slice:��:2��}} ���� [3,9]{{ 'asdikfjhihgie' | slice:':5' }} ���� ��asdik��  |
| slugify	  | ���ַ��������¼��ź��»��ߣ���������ɾ�����ո��ü����滻|	{{ '5-2=3and5 2=3' | slugify }} ���� 5-23and5-23 |
| stringformat	  | �ַ�����ʽ�����﷨ͬpython	 |                                                                               | 
| time	          | �������ڵ�ʱ�䲿��	 |                                                                                       |
| timesince	  | �ԡ�������Ϊֹ���˶೤ʱ�䡱��ʾʱ�����|	�������Ϊ 45days, 3 hours                                       |
| timeuntil	  | �ԡ������ڿ�ʼ��ʱ����������ж೤ʱ����ʾʱ�����|	                                                         |
| title	          | ÿ����������ĸ��д	 |                                                                                       |
| truncatewords	  | ���ַ���ת��Ϊʡ�Ա�﷽ʽ|	{{ 'This is a pen' | truncatewords:2 }}����                                      |
| This is ...     |                                                                                                              |
| truncatewords_html|ͬ�ϣ����������е�HTML��ǩ|	 {{ '<p>This is a pen</p>' | truncatewords:2 }}����<p>This is ...</p>    |
| urlencode	  | ���ַ����е������ַ�ת��Ϊurl���ݱ�﷽ʽ|	{{ ��http://www.aaa.com/foo?a=b&b=c�� | urlencode}}              |
| urlize          | �������ַ����е�url�ɴ��ı���Ϊ����	 |                                                                       |
| wordcount	  | ���ر����ַ����еĵ�����	 |                                                                               |
| yesno	          | ����������ת��Ϊ�ַ���yes, no ��maybe|   {{ True | yesno }}<br>                                             |
                                                             {{ False | yesno }}<br>                                            
                                                             {{ None | yesno }}<br>                                             
                                                             ����<br>                                                            
                                                             yes<br>                                                             
                                                             no<br>                                                              
                                                             maybe<br>                                                          

== 例示 ==

{| class="wikitable" border=1 cellspacing=2 cellpadding=5 
! 图例 !! 说明 !! 不可选 !! 可选 !! 已选
|-
|[[File:Prim_Algorithm_0.svg|200px]]
|此为原始的加权连通图。每条边一侧的数字代表其权值。
| - 
| -
| -
|-
|[[File:Prim_Algorithm_1.svg|200px]]
|[[顶点 (图论)|顶点]]'''D'''被任意选为起始点。顶点'''A'''、'''B'''、'''E'''和'''F'''通过单条边与'''D'''相连。'''A'''是距离'''D'''最近的顶点，因此将'''A'''及对应边'''AD'''以高亮表示。
| C, G
| A, B, E, F
| D
|-
|[[File:Prim_Algorithm_2.svg|200px]]
|下一个顶点为距离'''D'''或'''A'''最近的顶点。'''B'''距'''D'''为9，距'''A'''为7，'''E'''距'''D'''為15，'''F'''距'''D'''為6。因此，'''F'''距'''D'''或'''A'''最近，因此将顶点'''F'''与相应边'''DF'''以高亮表示。
| C, G
| B, E, F
| A, D
|-
|[[File:Prim Algorithm 3.svg|200px]]
|算法继续重复上面的步骤。距离'''A'''为7的顶点'''B'''被高亮表示。
| C
| B, E, G
| A, D, F
|-
|[[File:Prim Algorithm 4.svg|200px]]
|在当前情况下，可以在'''C'''、'''E'''与'''G'''间进行选择。'''C'''距'''B'''为8，'''E'''距'''B'''为7，'''G'''距'''F'''为11。'''E'''最近，因此将顶点'''E'''与相应边'''BE'''高亮表示。
| 无
| C, E, G
| A, D, F, B
|-
|[[File:Prim Algorithm 5.svg|200px]]
|这里，可供选择的[[顶点 (图论)|顶点]]只有'''C'''和'''G'''。'''C'''距'''E'''为5，'''G'''距'''E'''为9，故选取'''C'''，并与边'''EC'''一同高亮表示。
| 无
| C, G
| A, D, F, B, E
|-
|[[File:Prim Algorithm 6.svg|200px]]
|顶点'''G'''是唯一剩下的顶点，它距'''F'''为11，距'''E'''为9，'''E'''最近，故高亮表示'''G'''及相应边'''EG'''。
| 无
| G
| A, D, F, B, E, C
|-
|[[File:Prim Algorithm 7.svg|200px]]
|现在，所有[[顶点 (图论)|顶点]]均已被选取，图中绿色部分即为连通图的[[最小生成树]]。在此例中，最小生成树的权值之和为39。
| 无
| 无
| A, D, F, B, E, C, G
|}
#include <bits/stdc++.h>
using namespace std;

// ====== I/O 座標系切替 ======
// 入力が (x y)=(列 行) の順なら 1、(i j)=(行 列) の順なら 0
#ifndef IO_USES_XY
#define IO_USES_XY 1
#endif

struct Pos { int i, j; };

int N, TI, TJ;
vector<string> baseGrid;             // 初期 '.' or 'T'
vector<vector<char>> isCorridor;     // 回廊（保護通路）
vector<vector<char>> placed;         // 追加で置いた木
vector<vector<char>> confirmed;      // 確認済みフラグ

int SI, SJ; // 入口 (0, floor(N/2))

inline bool inb(int i, int j){ return 0 <= i && i < N && 0 <= j && j < N; }

// その時点の木判定（外周は木）
inline bool isTree(int i, int j){
    if(!inb(i,j)) return true;
    if(baseGrid[i][j] == 'T') return true;
    if(placed[i][j]) return true;
    return false;
}

// 初期マップのみで BFS 最短路（回廊の初期化に使用）
vector<Pos> bfs_path_initial(const Pos& s, const Pos& t){
    static const int di[4]={-1,1,0,0}, dj[4]={0,0,-1,1};
    vector<vector<int>> dist(N, vector<int>(N, -1));
    vector<vector<Pos>> prv(N, vector<Pos>(N, {-1,-1}));
    queue<Pos> q;
    dist[s.i][s.j]=0; q.push(s);
    while(!q.empty()){
        auto p=q.front(); q.pop();
        if(p.i==t.i && p.j==t.j) break;
        for(int d=0; d<4; ++d){
            int ni=p.i+di[d], nj=p.j+dj[d];
            if(!inb(ni,nj)) continue;
            if(dist[ni][nj]!=-1) continue;
            if(baseGrid[ni][nj]=='T') continue; // 初期木は通れない
            dist[ni][nj]=dist[p.i][p.j]+1;
            prv[ni][nj]=p;
            q.push({ni,nj});
        }
    }
    vector<Pos> path;
    if(dist[t.i][t.j]==-1) return path; // 入力保証上は到達可
    Pos cur=t;
    while(!(cur.i==s.i && cur.j==s.j)){
        path.push_back(cur);
        cur=prv[cur.i][cur.j];
    }
    path.push_back(s);
    reverse(path.begin(), path.end());
    return path;
}

// そのターンの位置 (pi,pj) から、dir 方向の視線上で
// 「未確認 && 回廊外 && まだ木でない」最手前セルを探す
// dir: 0=U,1=D,2=L,3=R
Pos first_unconfirmed_off_corridor_on_ray(int pi, int pj, int dir){
    static const int di[4]={-1,1,0,0}, dj[4]={0,0,-1,1};
    int ci=pi, cj=pj;
    while(true){
        ci+=di[dir]; cj+=dj[dir];
        if(!inb(ci,cj) || isTree(ci,cj)) break; // 木に当たるまで
        if(!confirmed[ci][cj] && !isCorridor[ci][cj]) return {ci,cj};
    }
    return {-1,-1};
}

vector<Pos> random_unconfirmed_samples(int need, mt19937 &rng){
    vector<Pos> cand; cand.reserve(N*N);
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            if(isCorridor[i][j]) continue;
            if(confirmed[i][j]) continue;
            if(isTree(i,j)) continue;
            cand.push_back({i,j});
        }
    }
    if(cand.empty()) return {};
    shuffle(cand.begin(), cand.end(), rng);
    if((int)cand.size()>need) cand.resize(need);
    return cand;
}

struct Planner{
    void init_corridor(){
        auto path = bfs_path_initial({SI,SJ}, {TI,TJ});
        isCorridor.assign(N, vector<char>(N, 0));
        for(auto &p: path) isCorridor[p.i][p.j]=1;
    }
    void replan_if_needed(){
        // SA 導入時に差し替え可。今は何もしない。
    }
} planner;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> TI >> TJ;
    baseGrid.resize(N);
    for(int i=0;i<N;++i) cin >> baseGrid[i];

    SI=0; SJ=N/2;
    placed.assign(N, vector<char>(N, 0));
    confirmed.assign(N, vector<char>(N, 0));
    planner.init_corridor();

    mt19937 rng(712367);

    while(true){
        int pi, pj, n;

#if IO_USES_XY
        // 入力 (x y) = (列 行)
        int px, py;
        if(!(cin >> px >> py >> n)) return 0;
        pi = py; pj = px; // (i,j) に変換
#else
        if(!(cin >> pi >> pj >> n)) return 0;
#endif
        vector<Pos> newly(n);
        for(int k=0;k<n;++k){
#if IO_USES_XY
            int x,y; cin >> x >> y;
            newly[k].i = y; newly[k].j = x; // 変換
#else
            cin >> newly[k].i >> newly[k].j;
#endif
        }

        // revealed 反映
        for(auto &p: newly){
            if(inb(p.i,p.j)) confirmed[p.i][p.j]=1;
        }

        // 花に到達なら終了
        if(pi==TI && pj==TJ) return 0;

        // replan フック（今は空）
        planner.replan_if_needed();

        // JIT 候補収集：4方向の最手前（回廊外・未確認）
        vector<Pos> outCells; outCells.reserve(16);
        for(int d=0; d<4; ++d){
            auto p = first_unconfirmed_off_corridor_on_ray(pi, pj, d);
            if(p.i!=-1){
                if(!isCorridor[p.i][p.j] && !confirmed[p.i][p.j] && !isTree(p.i,p.j)){
                    outCells.push_back(p);
                }
            }
        }

        // ランダム補助（序盤寄り）
        int bonus = max(0, N/8);
        auto rnds = random_unconfirmed_samples(bonus, rng);
        for(auto &p: rnds){
            if(!isCorridor[p.i][p.j] && !isTree(p.i,p.j)) outCells.push_back(p);
        }

        // 重複除去
        sort(outCells.begin(), outCells.end(),
             [](const Pos&a, const Pos&b){ return (a.i!=b.i)? a.i<b.i : a.j<b.j; });
        outCells.erase(unique(outCells.begin(), outCells.end(),
                              [](const Pos&a, const Pos&b){ return a.i==b.i && a.j==b.j; }),
                       outCells.end());

        // 最終ガード：revealed/回廊/既木 を除外（ここが重要）
        vector<Pos> finalOut; finalOut.reserve(outCells.size());
        for(auto &p: outCells){
            if(!inb(p.i,p.j)) continue;
            if(isCorridor[p.i][p.j]) continue;
            if(confirmed[p.i][p.j]) continue; // ここで確実に弾く
            if(isTree(p.i,p.j)) continue;
            finalOut.push_back(p);
        }

        // 反映
        for(auto &p: finalOut) placed[p.i][p.j]=1;

        // 出力（可視化/テスターの期待順に合わせる）
        cout << (int)finalOut.size();
        for(auto &p: finalOut){
#if IO_USES_XY
            cout << ' ' << p.j << ' ' << p.i; // (x y)
#else
            cout << ' ' << p.i << ' ' << p.j; // (i j)
#endif
        }
        cout << '\n' << flush;
    }
    return 0;
}

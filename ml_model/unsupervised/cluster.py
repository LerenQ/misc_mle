import numpy as np
from collections import defaultdict

class Kmeans:

    def __init__(self, dataset, k:int, centroids='kmeans', random_seed = None):
        '''
        Inputs: data, number of clusters, and initial centroids(kmeans or kmeans++)
        Outputs: dictionary including two elements: centers locs, and labeled data
        '''

        self.data = dataset
        self.data_labelled = None
        self.num_clusters = k
        self.kpp = 1 if centroids == 'kmeans++' else 0
        self.random_seed = random_seed
        self.tolerance = 0
        self.center = {}

    def measure(self, d):
        return np.linalg.norm(d, axis=0)

    def fit(self):
        iter = 0
        loss = {}
        delta = float('inf')

        # initialiate the centroids
        if self.kpp == 1:
            # kmeans++ selection
            self.kmeanspp()
        else:
            # random selection
            for k,v in enumerate(self.data[np.random.randint(len(self.data), size=self.num_clusters),:]):
                self.center[k] = v

        while delta > self.tolerance:
            distance = []
            cluster = defaultdict(list)
            for n, (x, y) in enumerate(self.data):
                # generate distances to all centers
                dist_list = self.measure([[x-self.center[i][0] for i in range(self.num_clusters)], 
                [y-self.center[i][1] for i in range(self.num_clusters)]])
                # record selection and corresponding distance 
                cluster[np.argmin(dist_list)].append((x,y))
                distance.append(min(dist_list))

            # iteration evaluation
            loss[iter] = sum(distance)
            if iter > 0:
                delta = loss[iter-1] - loss[iter]

            # new centroids
            for k,v in cluster.items():
                self.center[k] = np.average(v, axis=0)

            iter += 1

        return self.center, loss[iter-1]

    def predict(self, cords_array):
        y_pred = []
        for (x, y) in cords_array:
            dist_list = self.measure([[x-self.center[i][0] for i in range(self.num_clusters)], 
            [y-self.center[i][1] for i in range(self.num_clusters)]])
            y_pred.append(np.argmin(dist_list))
        y_pred = np.array(y_pred)
        self.data_labelled = np.concatenate((self.data, y_pred[:, np.newaxis]), axis=1)
        return y_pred, self.data_labelled

    def k_analys(self):
        wcss = []
        for i in range(1, 11):
            kmeans = Kmeans(self.data, k=i, random_seed = 4)
            _, l = kmeans.fit()
            wcss.append(l)
        self.center = {}

        return wcss

    def kmeanspp(self):
        # update self.center based on kmeans++
        self.center[0] = self.data[np.random.randint(len(self.data), size=1)[0]]
        n = 1
        while len(self.center) < self.num_clusters:
            dist = []
            for _, (x, y) in enumerate(self.data):
                d = self.measure([[x - self.center[i][0] for i in range(len(self.center))], 
                    [y - self.center[i][1] for i in range(len(self.center))]]
                    )
                dist.append(min(d))
            next = max(range(len(self.data)), key=lambda x: dist[x])
            self.center[n] = self.data[next]
            n += 1

            
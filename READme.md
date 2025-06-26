# AI-Based Subnet Resizing for Fleet Telematics


#Project overview
The exponential growth of IoT-enabled fleet vehicles presents a major challenge in managing IPv4 addresses efficiently. Despite IPv4 offering approximately 4.3 billion unique addresses, this space is becoming increasingly inadequate due to the rapid surge in connected devices. Although IPv6 was designed to overcome this limitation with a vastly larger address space, its adoption remains limited due to incompatibility with IPv4, high migration costs, and lack of support in many industrial hardware systems.

Consequently, optimizing IPv4 utilization remains a critical need, especially in the near term for connected transportation systems. This paper proposes a machine learning–based dynamic network resizing architecture for efficient IPv4 address allocation in large-scale fleet telematics environments. The architecture enables dynamic resizing of subnets using Classless Inter-Domain Routing (CIDR) and Variable Length Subnet Masking (VLSM), guided by adaptive supernet boundary suggestions based on regional payload and mobility patterns.

Dynamic Host Configuration Protocol (DHCP) is used to manage IP address leasing, while machine learning models enable real-time scalability and efficient address utilization. Theoretical analysis suggests that the proposed approach offers significant scalability and flexibility benefits under varying fleet densities.

The proposed framework is broadly applicable across various connected systems, including GNSS-enabled On-Board Units (OBUs) in fleet vehicles, smart transportation infrastructure, logistics and supply chain networks, connected public transit systems, and industrial IoT deployments—where dynamic IP allocation, mobility-aware subnet resizing, and real-time cloud-based coordination are essential for efficient network scalability.


# Project Link
All implementation steps, including data preprocessing, clustering, prediction modeling, and subnet resizing logic, are executed in a Jupyter Notebook (.ipynb) file, which contains the complete experimental workflow and result visualizations.
1. Dataset clean and pre-processing with focus on China geo boundary, normalization and standarzation techniques- https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/01_DatasetVisualize.ipynb
2. Explore the neighbouring taxi radius tuning parameters, downsized data set and its limitations with Density based clustering logic - https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/02_DBSCAN_ul.ipynb
3. Feature scalling (3d - spatio temporal changes), UMAP(GPU usage) - to reduce dimensions and predict. Fine tuning the time scale with 11/3 multiplication reduced the outliers and yeilded more clusters. ->  https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/03_HDBSCAN_ul.ipynb. HDBSCAN with gpu -> https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/03_HDBSCAN_ul_gpu.ipynb
4. Explore soft clustering using problemisitic membership using Gaussian Mixture Mode. - https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/04_GMM_ul.ipynb
5. Explore dendrograms https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/05_Hierarchical%20Clustering_ul.ipynb
6. baseline and Random forest classification method. -> https://github.com/leeprasath/IEEE_SubResizeUsingAIForFleetVehicles/blob/main/notebook/07_PreparePredictionModel.ipynb

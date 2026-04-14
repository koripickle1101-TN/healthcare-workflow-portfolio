-- VOL EDGE RCM: NET COLLECTION RATIO AUDIT
-- OBJECTIVE: Calculate financial performance across facility branches.

SELECT 
    Facility_Name,
    SUM(Gross_Charges) AS Total_Charges,
    SUM(Contractual_Adjustments) AS Total_Adjustments,
    SUM(Payments_Received) AS Total_Collections,
    
    -- NET COLLECTION RATIO CALCULATION
    ROUND(
        (SUM(Payments_Received) / NULLIF(SUM(Gross_Charges) - SUM(Contractual_Adjustments), 0)) * 100, 
    2) AS Net_Collection_Ratio

FROM 
    RCM_Performance_Data
WHERE 
    Service_Date BETWEEN '2026-01-01' AND '2026-03-31'
GROUP BY 
    Facility_Name
HAVING 
    Net_Collection_Ratio < 95;

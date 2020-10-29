// Place your custom css/js logic here
import React from 'react';

export {};

interface IColumnDetector {
    type: string;
    priority: number;
    checker: (colName: string, values: any[]) => boolean;
}

interface IColumnStatsAnalyzer {
    key: string;
    name: string;
    appliesToType: string[];
    generator: (values: any[]) => string;
}

interface IColumnTransformer {
    key: string;
    name: string;

    appliesToType: string[];
    priority: number;
    auto: boolean;

    transform: (v: any) => React.ReactNode;
}

// Use the following definitions to override default DataHub
// behavior
declare global {
    /* tslint:disable:interface-name */
    interface Window {
        // Users will see this message if they cannot
        // access any
        NO_ENVIRONMENT_MESSAGE?: string;
        CUSTOM_COLUMN_STATS_ANALYZERS?: IColumnStatsAnalyzer[];
        CUSTOM_COLUMN_DETECTORS?: IColumnDetector[];
        CUSTOM_COLUMN_TRANSFORMERS?: IColumnTransformer[];
    }
}
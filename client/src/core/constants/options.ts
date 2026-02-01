import { enumWithLabelToOptions } from "../enums/enum";
import { SituacoesOcorrencia, TiposOcorrencia } from "../enums/ocorrencia-enum";

export const SituacoesOcorrenciaLabel: Record<SituacoesOcorrencia, string> = {
  [SituacoesOcorrencia.AguardandoAnalise]: "Aguardando análise",
  [SituacoesOcorrencia.AcaoPedagogicaRealizada]: "Ação pedagógica realizada",
  [SituacoesOcorrencia.Finalizada]: "Finalizada",
};

export const SITUACAO_OCORRENCIA_OPTIONS = enumWithLabelToOptions(
  SituacoesOcorrencia,
  SituacoesOcorrenciaLabel
);

export const TiposOcorrenciaLabel: Record<TiposOcorrencia, string> = {
  [TiposOcorrencia.Comportamento]: "Comportamento",
  [TiposOcorrencia.Saude]: "Saúde",
  [TiposOcorrencia.Convivencia]: "Convivência",
  [TiposOcorrencia.Acidente]: "Acidente",
};

export const TIPO_OCORRENCIA_OPTIONS = enumWithLabelToOptions(
  TiposOcorrencia,
  TiposOcorrenciaLabel
);

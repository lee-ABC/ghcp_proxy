import unittest

from proxy_client_config import ProxyClientConfigService, _model_token_pricing_description


class ReasoningLevelTests(unittest.TestCase):
    def setUp(self):
        self.service = object.__new__(ProxyClientConfigService)

    def _effort_names(self, model_name, raw_efforts):
        levels, _ = self.service._resolve_reasoning_levels(
            "gpt", raw_efforts, model_name=model_name
        )
        return [level["effort"] for level in levels]

    def test_excel_models_never_expose_max(self):
        raw_efforts = ["low", "medium", "high", "xhigh", "max"]
        for model_name in (
            "gpt-5.6-luna-excel",
            "gpt-5.6-terra-excel",
            "gpt-5.6-sol-excel",
            "gpt-6-excel",
        ):
            with self.subTest(model_name=model_name):
                self.assertEqual(
                    self._effort_names(model_name, raw_efforts),
                    ["low", "medium", "high", "xhigh"],
                )

    def test_gpt_6_excel_catalog_keeps_existing_model_order(self):
        old_order = [
            "gpt-6-astra-excel", "gpt-5.6-sol-excel",
            "gpt-5.6-terra-excel", "gpt-5.6-luna-excel",
        ]
        models = self.service._sorted_catalog_model_names(set(old_order + ["gpt-6-excel"]))
        self.assertEqual(models, ["gpt-6-excel"] + old_order)

    def test_gpt_6_excel_uses_excel_subscription_description(self):
        self.assertEqual(
            _model_token_pricing_description("gpt-6-excel"),
            _model_token_pricing_description("gpt-5.6-sol-excel"),
        )

    def test_non_excel_gpt_56_still_exposes_max(self):
        self.assertEqual(
            self._effort_names(
                "gpt-5.6-sol", ["low", "medium", "high", "xhigh"]
            ),
            ["low", "medium", "high", "xhigh", "max"],
        )


if __name__ == "__main__":
    unittest.main()
